from unittest.mock import Mock, call
from core.scraper import Scraper
from tests.mocks.mocks import *

class TestScraper: 
    def create_scraper(self): 
        client = Mock(
            base_url="[BASE_URL]",
            prefix="[PREFIX]"
        )

        scraper = Scraper(
            client=client,  
            download_outdir="[DOWNLOAD_OUTDIR]",
            output_filename=Mock(side_effect=lambda p, t: f"{p}.{t}")
        )

        return scraper, client

    def test_constructor(self):
        scraper, client = self.create_scraper()
        assert client.base_url == "[BASE_URL]"
        assert client.prefix == "[PREFIX]"
        assert client.download_outdir == "[DOWNLOAD_OUTDIR]"

        assert scraper.client is client
        assert scraper.download_outdir == "[DOWNLOAD_OUTDIR]"
        assert scraper.output_filename("A", "B") == "A.B"

    def test_add(self): 
        scraper, client = self.create_scraper() 
    
        scraper.add("[ITEM-A]")

        assert len(scraper.items) == 1 
        assert scraper.items[0] == "[ITEM-A]"

        scraper.add("[ITEM-B]")

        assert len(scraper.items) == 2
        assert scraper.items[1] == "[ITEM-B]"

        scraper.add("[ITEM-C]")

        assert len(scraper.items) == 3
        assert scraper.items[2] == "[ITEM-C]"

    def test_add_multi(self): 
        scraper, client = self.create_scraper() 

        scraper.add_multi(["ITEM-A1", "ITEM-B1", "ITEM-C1"])

        assert len(scraper.items) == 3 
        assert scraper.items[0] == "ITEM-A1"
        assert scraper.items[1] == "ITEM-B1"
        assert scraper.items[2] == "ITEM-C1"

        scraper.add_multi(["ITEM-A2", "ITEM-B2", "ITEM-C2"])

        assert len(scraper.items) == 6
        assert scraper.items[3] == "ITEM-A2"
        assert scraper.items[4] == "ITEM-B2"
        assert scraper.items[5] == "ITEM-C2"  

    def test_download(self): 
        scraper, client = self.create_scraper() 

        client.prefix = "[PREFIX]" 
        scraper.items = ["[ITEM-A]", "[ITEM-B]", "[ITEM-C]"]

        scraper.output_filename = Mock(
            side_effect=[
                "[NAME-A]", 
                "[NAME-B]", 
                "[NAME-C]"
            ]
        )

        scraper.scrape()

        assert len(scraper.client.download.call_args_list) == 3 

        scraper.client.download.assert_has_calls([
            call('[ITEM-A]', '[NAME-A]'),
            call('[ITEM-B]', '[NAME-B]'),
            call('[ITEM-C]', '[NAME-C]')
        ])