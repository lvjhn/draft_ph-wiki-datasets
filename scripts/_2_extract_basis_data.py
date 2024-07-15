import scripts._0_config as config

from core.basis_articles.igba import IslandGroupBasisArticle 
from core.basis_articles.rba import RegionBasisArticle
from core.basis_articles.pba import ProvinceBasisArticle 
from core.basis_articles.dba import DistrictBasisArticle 
from core.basis_articles.cba import CityBasisArticle
from core.basis_articles.mba import MunicityBasisArticle

# parameters
CONTEXT = config.CONTEXT
INPUT_FOLDER = f"./data/{CONTEXT}/articles/basis/"
OUTPUT_FOLDER = f"./data/{CONTEXT}/metadata/basis/"

# island-groups
print("@ Processing island-groups.")
igba = IslandGroupBasisArticle(folder=INPUT_FOLDER) 
igba.extract_metas().to_csv(OUTPUT_FOLDER + "/island-groups.csv")

# regions
print("@ Processing regions.")
rba = RegionBasisArticle(folder=INPUT_FOLDER) 
rba.extract_metas().to_csv(OUTPUT_FOLDER + "/regions.csv")

# provinces
print("@ Processing provinces.")
pba = ProvinceBasisArticle(folder=INPUT_FOLDER) 
pba.extract_metas().to_csv(OUTPUT_FOLDER + "/provinces.csv")

# districts
print("@ Processing districts.")
dba = DistrictBasisArticle(folder=INPUT_FOLDER) 
dba.extract_metas().to_csv(OUTPUT_FOLDER + "/districts.csv")

# municities
print("@ Processing cities.")
cba = CityBasisArticle(folder=INPUT_FOLDER) 
cba.extract_metas().to_csv(OUTPUT_FOLDER + "/cities.csv")

# municities
print("@ Processing municities.")
mba = MunicityBasisArticle(folder=INPUT_FOLDER) 
mba.extract_metas().to_csv(OUTPUT_FOLDER + "/municities.csv")


