import core.helpers as helpers
from bs4 import BeautifulSoup
from svgpath2mpl import parse_path
from shapely import MultiPolygon
import svgwrite 

from core.map import Map

class SVGMap(Map):
    def __init__(self, *args, **kwargs):
        Map.__init__(self, *args, **kwargs)
        self.admin_level = kwargs.get("admin_level", "regions")
        self.folder = kwargs.get("folder", "./data/2024-JULY/maps/raw/svg")
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

    def components(self): 
        paths = self.content.select("path")
        components = {} 
        for path in paths: 
            components[path["id"]] = \
                path.attrs 
            components[path["id"]]["polygons"] = \
                parse_path(path["d"]).to_polygons()
            
        return components

    def union_by_attribute(self, attr): 
        components = self.components() 
        grouped_items = {}

        for key in components:
            component = components[key]
            group_attr = component[attr]
            if group_attr not in grouped_items:
                grouped_items[group_attr] = [] 
            grouped_items[group_attr].append(component)
            

        for item in grouped_items:
            group = grouped_items[item]
            print(len(group))

        return components 

    def union_by_attributes(self):
        pass

    def exterior_components(self): 
        pass 

    def interior_components(self): 
        pass 

    def adjacency_list(self): 
        pass 

    def uncache(self):
        pass 

    def preload(self): 
        pass 
    
    def draw_svg(self, outfile, **kwargs): 
        dw = \
            svgwrite.Drawing(
                filename=outfile, 
                **kwargs
            )

        components = self.components() 
        for key in components:
            component = components[key]
            polygons = component["polygons"]
            for polygon in polygons:
                dw.add(
                    dw.polygon(polygon, id=component["id"])
                )

        dw.save()
    