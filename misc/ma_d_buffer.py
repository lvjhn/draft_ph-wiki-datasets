import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.da import DistrictArticle

da = DistrictArticle(
    "Camarines_Sur__3", 
    folder="./misc/data/main-articles/districts/"
) 

fields = da.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

