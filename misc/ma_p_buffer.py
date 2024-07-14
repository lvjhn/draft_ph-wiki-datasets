import core.helpers as helpers

helpers.DEBUG = True

from core.main_articles.pa import ProvinceArticle

pa = ProvinceArticle(
    "Camarines_Sur", 
    folder="./misc/data/main-articles/provinces/"
) 

fields = pa.extract_all()

for field in fields:
    print(f"{field} = {fields[field]}")
    print()

