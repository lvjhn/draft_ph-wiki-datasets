import scripts._0_config as config 

from core.client import Client 
from core.scraper import Scraper 

CONTEXT = config.CONTEXT

items = [
    (
        "Island_groups_of_the_Philippines", 
        "Philippines (Island Groups)"
    ), 
    (
        "Regions_of_the_Philippines", 
        "Philippines (Regions)"
    ),
    (
        "Provinces_of_the_Philippines",
        "Philippines (Provinces)"
    ),
    ( 
        "Congressional_districts_of_the_Philippines",
        "Philippines (Districts)"
    ),
    ( 
        "List_of_cities_in_the_Philippines",
        "Philippines (Cities)"
    ),
    ( 
        "List_of_cities_and_municipalities_in_the_Philippines",
        "Philippines (Municities)"
    )
]

wikipedia_client = Client(
    base_url="https://en.wikipedia.org", 
    prefix="wiki"
)

scraper = Scraper(
    client=wikipedia_client,
    download_outdir=f"./data/{CONTEXT}/articles/basis",
    output_filename=lambda prefix, tail, index: items[index][1] + ".html"
)

for item in items:
    scraper.add(item[0])

scraper.scrape(verbose=True)

print("@ Done.")
