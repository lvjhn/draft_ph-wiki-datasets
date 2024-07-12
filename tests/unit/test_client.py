from unittest.mock import Mock 
from core.client import Client
from tests.mocks.mocks import *

class TestClient: 
    def test_constructor(self):
        client = Client(
            base_url="example.com",
            prefix="/prefix", 
            download_outdir="./data/downloads"
        )

        assert client.base_url == "example.com" 
        assert client.prefix  == "/prefix"
        assert client.download_outdir == "./data/downloads"

    def test_get_output_filename_no_kw_args(self): 
        client = Client() 
        assert client.get_output_filename("item") == "item.html"

    def test_get_output_filename_with_extension(self): 
        client = Client() 
        assert client.get_output_filename(
            "item", extension="txt"
        ) == "item.txt"

    def test_get_output_filename_manual_outfile(self): 
        client = Client() 
        assert client.get_output_filename(
            "item", outfile="renamed.txt"
        ) == "renamed.txt"
    
    def test_get_full_url(self):
        client = Client(base_url="a", prefix="b")
        assert client.get_full_url("c") == "a/b/c"

    def test_data(self): 
        requests_mock = Mock() 
        requests_mock.get = Mock(return_value=Mock(text="[TEXT]"))

        client = Client(inject_requests=requests_mock)
        client.get_full_url = Mock(return_value="[URL]")

        text = client.data("[URI]")

        client.get_full_url.assert_called_with("[URI]")    
        requests_mock.get.assert_called_with("[URL]")    

        assert text == "[TEXT]"

    def test_download(self): 
        client = Client()

        client.get_output_filename = Mock(return_value="[OUTPUT_FILENAME]")
        client.get_full_url = Mock(return_value="[FULL_URL]")
        client.data = Mock(return_value="[TEXT]")
        client.save_to_file = Mock()

        client.download("[URI]") 

        client.get_output_filename.assert_called_with("[URI]", None, "html")
        client.get_full_url.assert_called_with("[URI]")
        client.data.assert_called_with("[FULL_URL]")
        client.save_to_file.assert_called_with("[OUTPUT_FILENAME]", "[TEXT]")   

    def test_save_to_file(self):
        client = Client(inject_open=open_mock) 
        client.save_to_file("[FILEPATH]", "[TEXT]")
        open_mock.assert_called_with("[FILEPATH]", "[TEXT]")