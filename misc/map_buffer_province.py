from core.maps.svg_map import SVGMap
from core.maps.geojson_map import GeoJSONMap
import json 
from core.locator import Locator

map_ = GeoJSONMap(
    admin_level="provinces.hires",
    cache=True,
    preload=True
) 

svg_map = SVGMap(
    admin_level="provinces",
    cache=True,
    preload=True
)

svg_map.components = svg_map.get_components()

adjacencies = map_.adjacency_list()

map_.components = map_.get_components()

for key in adjacencies: 
    try:
        key_name = list(Locator.province("GD/2024-JULY", code=key)["Province"])[0]
        key_iso = list(Locator.province("GD/2024-JULY", code=key)["ISO"])[0]
    except:
        continue

    print(key, key_name)
    neighbors_iso = []
    for neighbor in adjacencies[key].keys():
        try:
            neighbor_name = \
                list(Locator.province("GD/2024-JULY", code=neighbor)["Province"])[0]
            neighbor_iso = \
                list(Locator.province("GD/2024-JULY", code=neighbor)["ISO"])[0]
            print("\t", neighbor, neighbor_name)
            neighbors_iso.append(neighbor_iso)
        except:
            continue

    svg_map.draw_svg(
        f"./temp/{key_iso}.svg", 
        id_field="id", 
        highlights=[
            (set([key_iso]), "blue"),
            (set(neighbors_iso), "green")
        ],
        size=(10000, 10000)
    )
        