import json
import os
import scripts.GD._0_config as config 
import pandas as pd
from core.referencer import Referencer 

#
# CONFIGURATION
# 
CONTEXT = config.CONTEXT
OUTPUT_FOLDER = f"./data/{CONTEXT}/metadata/reference"

#
# MAIN SCRIPT 
#  
print("@ Extracting reference metadata.")

print("\tExtracting island groups.")
(
    Referencer
        .island_groups(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/island-groups.csv")
)

print("\tExtracting regions.")
(
    Referencer
        .regions(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/regions.csv")
)

print("\tExtracting provinces.")
(
    Referencer
        .provinces(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/provinces.csv")
)

print("\tExtracting districts.")
(
    Referencer
        .districts(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/districts.csv")
)

print("\tExtracting municipalities.")
(
    Referencer
        .municities(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/municities.csv")
)

print("\tExtracting barangays.")
(
    Referencer
        .barangays(CONTEXT)
        .to_csv(f"{OUTPUT_FOLDER}/barangays.csv")
)



print("@ Done.")