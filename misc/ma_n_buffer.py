import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.na import NationArticle

ma = NationArticle(
    "Philippines", 
    folder="./misc/data/main-articles/nation/"
) 

fields = ma.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

