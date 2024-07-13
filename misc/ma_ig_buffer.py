import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.iga import IslandGroupArticle

ma = IslandGroupArticle(
    "Luzon", 
    folder="./misc/data/main-articles/island-groups/"
) 

fields = ma.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

