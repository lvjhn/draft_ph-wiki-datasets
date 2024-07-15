from core.maps.svg_map import SVGMap

map_ = SVGMap(
    admin_level="provinces",
    cache=True
) 

map_.union_by_attribute("id")

map_.draw_svg("provinces.svg")

