import json
import os
import scripts._0_config as config

#
# CONFIGURATION
# 
CONTEXT       = config.CONTEXT
DATA_FOLDER   = "./data/" + CONTEXT + "/maps/raw/geojson"
OUTPUT_FOLDER = "./data/" + CONTEXT + "/maps/raw/geojson/combined"

#
# MAIN SCRIPT 
# 
def combine_maps(subcontext, output_name):
    print(f"@ Processing context {subcontext} -> {output_name}")
    subfolder = DATA_FOLDER + "/" + subcontext
    folder_items = os.listdir(subfolder) 
    outfile = open(OUTPUT_FOLDER + "/" + output_name + ".json", "w")

    combined = []
    
    i = 0
    n = len(folder_items)

    for folder_item in folder_items: 
        print(f"\t@ Processing {i + 1} of {n}", end="\r")
        infile = open(subfolder + "/" + folder_item).read()
        data = json.loads(infile)
        
        if "features" not in data: 
            continue

        features = data["features"] 
        
        combined += features
        i += 1

    print(f"\n\t@ Writing to file.", end="\r")

    json.dump(combined, outfile)

    return combined


#
# COMBINE ITEMS 
# 

# Regions
combine_maps("country/medres", "regions.medres")
combine_maps("country/lowres", "regions.lowres")
combine_maps("country/hires", "regions.hires")

# Provinces
combine_maps("regions/lowres", "provinces.lowres")
combine_maps("regions/medres", "provinces.medres")
combine_maps("regions/hires", "provinces.hires")

# Municipalities
combine_maps("provdists/lowres", "municities.lowres")
combine_maps("provdists/medres", "municities.medres")
combine_maps("provdists/hires", "municities.hires")

# Barangays
combine_maps("municities/lowres", "barangays.lowres")
combine_maps("municities/medres", "barangays.medres")
combine_maps("municities/hires", "barangays.hires")