from core.basis_articles.dba import DistrictBasisArticle

dba = DistrictBasisArticle(folder="./misc/data/basis-articles/") 

print(dba.extract_metas())
