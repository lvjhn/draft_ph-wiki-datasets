from unittest.mock import Mock 
from core.client import Client 
from core.scraper import Scraper 

import os

from core.basis_articles.igba import IslandGroupBasisArticle
from core.basis_articles.rba import RegionBasisArticle
from core.basis_articles.pba import ProvinceBasisArticle 
from core.basis_articles.dba import DistrictBasisArticle
from core.basis_articles.mba import MunicityBasisArticle

from .base_test import BaseTest
from io import StringIO  

REWRITE = False

class TestBasisArticles(BaseTest): 

    def check_match(self, metas, context): 
        global REWRITE
        if REWRITE: 
            metas.to_csv(f"./tests/data/basis-articles-outputs/{context}.csv")

        str_ = StringIO()
        metas.to_csv(str_)
        checker = \
            open(
                f"./tests/data/basis-articles-outputs/"
                f"{context}.csv"
            ).read()
        assert checker == str_.getvalue()

    def test_island_group_basis_articles(self):
        article = \
            IslandGroupBasisArticle(folder="./tests/data/basis-articles") 
        metas = \
            article.extract_metas() 

        assert metas.shape == (3, 11)

        self.check_match(metas, "island-groups")
 

    def test_region_basis_articles(self):
        article = \
            RegionBasisArticle(folder="./tests/data/basis-articles") 
        metas = \
            article.extract_metas() 
        
        assert metas.shape == (18, 14)

        self.check_match(metas, "regions")

    def test_province_basis_articles(self):
        article = \
            ProvinceBasisArticle(folder="./tests/data/basis-articles") 
        metas = \
            article.extract_metas() 
        
        assert metas.shape == (83, 19)

        self.check_match(metas, "provinces")

    def test_district_basis_articles(self):
        article = \
            DistrictBasisArticle(folder="./tests/data/basis-articles") 
        metas = \
            article.extract_metas() 
        
        assert metas.shape == (253, 10)

        self.check_match(metas, "districts")

    def test_municity_basis_articles(self):
        article = \
            MunicityBasisArticle(folder="./tests/data/basis-articles") 
        metas = \
            article.extract_metas() 
        
        assert metas.shape == (1642, 7)

        self.check_match(metas, "municities")
