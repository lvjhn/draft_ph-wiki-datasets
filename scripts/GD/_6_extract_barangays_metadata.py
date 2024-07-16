import json
import os
import scripts.GD._0_config as config 
import pandas as pd

#
# CONFIGURATION
# 
CONTEXT = config.CONTEXT
INPUT_FOLDER = "./data/" + CONTEXT + "/maps/raw/geojson/combined"
OUTPUT_FOLDER = "./data/" + CONTEXT + "/metadata/basis"
INPUT_FILE = INPUT_FOLDER + "/barangays.lowres.json"
OUTPUT_FILE = OUTPUT_FOLDER + "/barangays.csv"

#
# MAIN SCRIPT 
#  
print("@ Loading barangays.lowres.json file.")
barangays = json.load(open(INPUT_FILE, "r")) 
columns = list(barangays[0]["properties"].keys())
rows = []
for i in range(len(barangays)):
    print(f"\t@ Processing {i} of {len(barangays)} barangays.", end="\r") 
    rows.append(barangays[i]["properties"])
print()

print("@ Saving to CSV file.")
df = pd.DataFrame(rows, columns=columns)
df.to_csv(OUTPUT_FILE)

print("@ Done.")