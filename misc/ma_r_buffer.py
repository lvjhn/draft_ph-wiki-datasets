import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.ra import RegionArticle

ra = RegionArticle(
    "Bicol_Region", 
    folder="./misc/data/main-articles/regions/"
) 

fields = ra.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

