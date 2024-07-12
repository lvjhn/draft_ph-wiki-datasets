from unittest.mock import Mock 
from core.client import Client 
import os

from .base_test import BaseTest

class TestClient(BaseTest): 
    def test_client_download(self): 
        client = Client(download_outdir="./tests/temp")
        
        client.download("Article", "Article.html")

        assert os.path.exists("./tests/temp/Article.html")
        assert "Article" in open("./tests/temp/Article.html", "r").read()
