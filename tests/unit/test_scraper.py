from unittest.mock import Mock 
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
        