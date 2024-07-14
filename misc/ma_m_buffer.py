import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.ma import MunicipalityArticle

ma = MunicipalityArticle(
    "Calabanga", 
    folder="./misc/data/main-articles/municities/"
) 

fields = ma.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

