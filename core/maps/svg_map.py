import core.helpers as helpers
from bs4 import BeautifulSoup
from svgpath2mpl import parse_path
from shapely \
    import MultiPolygon, GeometryCollection, LineString, Polygon, \
           union_all, make_valid
import svgwrite 

from core.map import Map

class SVGMap(Map):
    def __init__(self, *args, **kwargs):
        Map.__init__(self, *args, **kwargs)
        self.admin_level = kwargs.get("admin_level", "regions")
        self.folder = kwargs.get("folder", "./data/GD/2024-JULY/maps/raw/svg")
        self.load_map_file()

    def load_map_file(self):
        file_path = self.folder + "/" + self.admin_level + ".svg"
        file_path = file_path.replace("//", "/")
        self.file_path = file_path
        self.content = \
            BeautifulSoup(
                open(file_path, "r").read(), 
                features="xml"
            )

    def get_components(self): 
        paths = self.content.select("path")
        components = {} 
        
        for path in paths: 
            components[path["id"]] = \
                path.attrs 
            components[path["id"]]["polygons"] = \
                parse_path(path["d"]).to_polygons()       

        return components

    