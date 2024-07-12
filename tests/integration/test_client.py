from unittest.mock import Mock 
from core.client import Client 
import os

class TestClient: 
    def test_client_download(self): 
        client = Client(download_outdir="./temp")
        
        client.download("Article", "Article.html")

        assert os.path.exists("./temp/Article.html")
        assert "Article" in open("./temp/Article.html", "r").read()
        os.unlink("./temp/Article.html")