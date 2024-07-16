from core.maps.svg_map import SVGMap
from core.maps.geojson_map import GeoJSONMap
import json 
from core.locator import Locator
from core.helpers import fix_mun_psgc, unfix_mun_psgc

map_ = GeoJSONMap(
    admin_level="municities.hires",
    cache=True,
    preload=True
) 

svg_map = SVGMap(
    admin_level="municities",
    cache=True,
    preload=True
)

exteriors = map_.exterior()

exteriors_psgc = set()
for exterior in exteriors:
    exterior = unfix_mun_psgc(str(exterior))
    try:
        exterior_name = \
            list(Locator.municity("GD/2024-JULY", code=exterior)["Municity"])[0]
        exterior_psgc = \
            list(Locator.municity("GD/2024-JULY", code=exterior)["PSGC"])[0]
        PSGC = str(exterior_psgc).replace(".0", "").zfill(9) 
        print("\t", PSGC, exterior_name)
        exteriors_psgc.add(
            "PH" + PSGC
        )
    except Exception as e:
        pass

svg_map.components = svg_map.get_components()
svg_map.draw_svg(
    f"./exteriors.svg", 
    id_field="data-municipality-psgc",
    highlights=[(exteriors_psgc, "green")],
    size=(20000,20000)
)
