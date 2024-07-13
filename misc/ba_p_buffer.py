from core.basis_articles.pba import ProvinceBasisArticle

pba = ProvinceBasisArticle(folder="./misc/data/basis-articles/") 

print(pba.extract_metas())
