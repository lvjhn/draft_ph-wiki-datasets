import scripts._0_config as config

from core.main_articles.na import NationArticle
from core.main_articles.iga import IslandGroupArticle 
from core.main_articles.ra import RegionArticle
from core.main_articles.pa import ProvinceArticle 
from core.main_articles.da import DistrictArticle 
from core.main_articles.ma import MunicityArticle

from core.client import Client
from core.scraper import Scraper

import pandas as pd

# parameters
CONTEXT = config.CONTEXT
BASIS_FOLDER = f"./data/{CONTEXT}/metadata/basis/"
ARTICLES_FOLDER = f"./data/{CONTEXT}/articles/main/"
OUTPUT_FOLDER = f"./data/{CONTEXT}/metadata/main/"

# scrape for context
def extract_for_context(context):
    print(f"@ ===== Extracting for context [{context}] =====")

    if context == "nation":
        na = NationArticle(
            article="Philippines", 
            folder=f"{ARTICLES_FOLDER}/nation"
        ) 
        data = na.extract_all()
        df = pd.DataFrame(
            [list(data.values())],
            columns=list(data.keys())
        )
        df.to_csv(f"{OUTPUT_FOLDER}/nation.csv")
    else:
        Article = None 
        
        if context == "island-groups":
            Article = IslandGroupArticle 
            name_field = "island_group"
        elif context == "regions":
            Article = RegionArticle
        elif context == "provinces": 
            Article = ProvinceArticle 
            name_field = "province"
        elif context == "districts": 
            Article = DistrictArticle
        elif context == "municities":
            Article = MunicityArticle

        basis_file = f"{BASIS_FOLDER}{context}.csv"
        basis = pd.read_csv(basis_file)
        columns = None
        rows = []
        n = len(basis)
        for index, row in basis.iterrows():
            print(f"\t@ Processing {row['Article Link']} ({index + 1} of {n})")
            article = Article(
                row["Article Link"].split("/")[2], 
                folder=f"{ARTICLES_FOLDER}{context}/"
            )

            data = article.extract_all() 

            if columns is None:
                columns = list(data.keys()) + ["Article Link"]

            rows.append(list(data.values()) + [row["Article Link"]])

        df = pd.DataFrame(rows, columns=columns)
        
        df.to_csv(f"{OUTPUT_FOLDER}/{context}.csv")


extract_for_context("nation")
extract_for_context("island-groups")
extract_for_context("regions")
extract_for_context("provinces")
extract_for_context("districts")
extract_for_context("municities")

print("@ Done.")
