from unittest.mock import Mock 
from core.client import Client 
from core.scraper import Scraper 
import json 

import os
from core.main_articles.na import NationArticle
from core.main_articles.iga import IslandGroupArticle
from core.main_articles.ra import RegionArticle
from core.main_articles.pa import ProvinceArticle 
from core.main_articles.da import DistrictArticle
from core.main_articles.ma import MunicityArticle

from .base_test import BaseTest
from io import StringIO  

REWRITE = False

class TestMainArticles(BaseTest): 

    def check_match(self, article, context): 
        global REWRITE
        folder = f"./tests/data/main-articles/{context}/"
        out_folder = f"./tests/data/main-articles-outputs/{context}/"
        out_file = out_folder + "/" + article.article + ".json"

        if REWRITE:
            json.dump(article.extract_all(), open(out_file, "w"), indent=4)

        stringified = json.dumps(article.extract_all(), indent=4)
        contents = open(out_file, "r").read() 
        
        assert stringified == contents 


    def test_nation_article(self):
        article = \
            NationArticle(
                "Philippines",
                folder="./tests/data/main-articles/nation"
            ) 
        
        self.check_match(article, "nation")

    def test_island_group_article(self):
        article = \
            IslandGroupArticle(
                "Luzon",
                folder="./tests/data/main-articles/island-groups"
            ) 
        
        self.check_match(article, "island-groups")

    def test_region_article(self):
        article = \
            RegionArticle(
                "Bicol_Region",
                folder="./tests/data/main-articles/regions"
            ) 
        
        self.check_match(article, "regions")

    def test_province_article(self):
        article = \
            ProvinceArticle(
                "Camarines_Sur",
                folder="./tests/data/main-articles/provinces"
            ) 
        
        self.check_match(article, "provinces")

    def test_district_article(self):
        article = \
            DistrictArticle(
                "Camarines_Sur__3",
                folder="./tests/data/main-articles/districts"
            ) 
        
        self.check_match(article, "provinces")


    def test_municity_article(self):
        article = \
            MunicityArticle(
                "Calabanga",
                folder="./tests/data/main-articles/municities"
            ) 
        
        self.check_match(article, "municities")

        article = \
            MunicityArticle(
                "Naga",
                folder="./tests/data/main-articles/municities"
            ) 
        
        self.check_match(article, "municities")

