from core.maps.svg_map import SVGMap
from core.maps.geojson_map import GeoJSONMap
import json 

map_ = GeoJSONMap(
    admin_level="barangays.lowres",
    cache=True,
    preload=True
) 

print(json.dumps(map_.adjacency_list(), indent=4))