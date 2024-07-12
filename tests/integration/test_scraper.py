from unittest.mock import Mock 
from core.client import Client 
from core.scraper import Scraper 
import os

from .base_test import BaseTest

class TestClient(BaseTest): 
    def test_client_download(self): 
        client = Client(
            base_url="https://en.wikipedia.org", 
            prefix="wiki"
        )

        scraper = Scraper(
            client = client,
            download_outdir="./tests/temp"
        )
        
        scraper.add("Word")
        scraper.add("Sentence")
        scraper.add("Paragraph")

        scraper.add_multi(["News", "Essay", "Article"]) 

        scraper.scrape()

        assert os.path.exists("./tests/temp/Word.html")
        assert os.path.exists("./tests/temp/Sentence.html")
        assert os.path.exists("./tests/temp/Paragraph.html")
        assert os.path.exists("./tests/temp/News.html")
        assert os.path.exists("./tests/temp/Essay.html")
        assert os.path.exists("./tests/temp/Article.html")


