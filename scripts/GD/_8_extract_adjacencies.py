import scripts.GD._0_config as config 

from core.locator import Locator
from core.maps.svg_map import SVGMap
from core.maps.geojson_map import GeoJSONMap

import pandas as pd
import json


#
# CONFIGURATION
# 
CONTEXT = config.CONTEXT
OUTPUT_FOLDER = f"./data/{CONTEXT}/maps/adjacencies"

#
# MAIN SCRIPT 
# 
flow = {
    "regions.lowres",
    "regions.medres",
    "regions.hires",

    "provinces.lowres",
    "provinces.medres",
    "provinces.hires",

    "municities.lowres",
    "municities.medres",
    "municities.hires",
    
    "barangays.lowres",
    "barangays.medres",
    "barangays.hires"
}


for item in flow: 
    print(f"@ ========== Processing GeoJSON Map [{item}] ==========")
    map_ = GeoJSONMap(
        admin_level=item,
        cache=True,
        preload=True
    )
    adjacencies = map_.adjacency_list()
    json.dump(
        adjacencies, 
        open(f"{OUTPUT_FOLDER}/lists/{item}.json", "w"),
        indent=4
    )
    
print("@ Done.")