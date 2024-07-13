from unittest.mock import Mock 

from core.article import Article 
from core.extractor import Extractor

import os

from .base_test import BaseTest

class TestArticle(BaseTest): 
    def create_article(self):
        return Article("Naga", folder="./tests/data/")

    def test_load_content(self): 
        article = self.create_article() 
        assert "Naga" in article.load_content() 
        assert "city" in article.load_content() 
        assert "Camarines Sur" in article.load_content() 

    def test_load_extractor(self): 
        article = self.create_article() 
        assert type(article.load_extractor()) is Extractor

    def test_constructor(self): 
        article = self.create_article() 
        assert type(article.extractor) is Extractor 
        assert type(article.content) is str 
        assert article.article == "Naga"
        assert article.folder == "./tests/data/"

    def test_constructor(self): 
        article = self.create_article() 
        assert type(article.extractor) is Extractor 
        assert type(article.content) is str 
        assert article.article == "Naga"
        assert article.folder == "./tests/data/"    
    
    def test_get_headers(self): 
        article = self.create_article() 
        assert len(article.get_headers(1)) == 1
        assert len(article.get_headers(2)) == 17
        assert len(article.get_headers(3)) == 32 
        assert len(article.get_headers(4)) == 11
        assert len(article.get_headers(5)) == 0
        assert len(article.get_headers(6)) == 0

    def test_introduction(self): 
        article = self.create_article() 
        content = article.introduction().get_text()
        sent = (
            "The town was established in 1575 by order of " 
            "Spanish Governor-General Francisco de Sande."
        )
        assert sent in content

    def test_top_level_sections(self): 
        article = self.create_article() 
        sections = article.top_level_sections()
        keys = list(sections.keys())
        values = list(sections.values())
        assert type(sections) is dict 
        assert type(keys[0]) is str 
        assert hasattr(values[0], "get_text") 
        assert len(keys) == 17

    def test_content_tree(self): 
        article = self.create_article() 

        tree = article.content_tree()

        assert type(tree) is dict 
        
        assert "Etymology" in tree
        assert "History" in tree
        assert "Geography" in tree

        assert "Precolonial era" in tree["History"]
        assert "Barangays" in tree["Geography"]
        assert "Magsaysay district" in tree["Economy"]

        assert "Roman Catholicism" in tree["Demographics"]["Religion"]
        assert "Isarog Agta Language" in tree["Demographics"]["Language"]
        assert "Kamundagan Festival" in tree["Culture"]["Festivals"]

    def test_subsection(self): 
        article = self.create_article() 
        subsection = \
            article.subsection(("History", "Precolonial era")).get_text()
        sentence = (
            "An ancient tomb preserved among the Bicolanos, "
            "discovered and examined by anthropologists during " 
            "the 1920s, refers to some of the same deities and "
            "personages mentioned in the Maragtas."
        )
        assert sentence in subsection