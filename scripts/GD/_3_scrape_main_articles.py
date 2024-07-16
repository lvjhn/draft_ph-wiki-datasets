import scripts.GD._0_config as config 

from core.basis_articles.igba import IslandGroupBasisArticle 
from core.basis_articles.rba import RegionBasisArticle
from core.basis_articles.pba import ProvinceBasisArticle 
from core.basis_articles.dba import DistrictBasisArticle 
from core.basis_articles.cba import CityBasisArticle
from core.basis_articles.mba import MunicityBasisArticle

from core.client import Client
from core.scraper import Scraper

import pandas as pd

# parameters
CONTEXT = config.CONTEXT
INPUT_FOLDER = f"./data/{CONTEXT}/metadata/basis/"
OUTPUT_FOLDER = f"./data/{CONTEXT}/articles/main/"

# create scraper
wikipedia_client = Client(
    base_url="https://en.wikipedia.org", 
    prefix="wiki"
)

# scrape for context
def scrape_for_context(context):
    print(f"@ ===== Scraping for context [{context}] =====")

    if context == "nation":
        scraper = Scraper(
            client=wikipedia_client
        )
        scraper.client.download_outdir = f"{OUTPUT_FOLDER}/nation/" 
        scraper.add("Philippines")
        scraper.scrape()

    else:
        scraper = Scraper(
            client=wikipedia_client
        )
        scraper.client.download_outdir = f"{OUTPUT_FOLDER}/{context}/" 
        basis = pd.read_csv(f"{INPUT_FOLDER}{context}.csv") 
        links = basis["Article Link"]        
        items = [link.split("/")[2] for link in links]
        scraper.add_multi(items)
        scraper.scrape(verbose=True)


scrape_for_context("nation")
scrape_for_context("island-groups")
scrape_for_context("regions")
scrape_for_context("provinces")
scrape_for_context("districts")
scrape_for_context("municities")

print("@ Done.")
