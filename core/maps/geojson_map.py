import core.helpers as helpers
import json 

from core.map import Map

class GeoJSONMap(Map):
    def __init__(self, *args, **kwargs):
        Map.__init__(self, *args, **kwargs)
        self.admin_level = kwargs.get("admin_level", "regions")
        self.folder = \
            kwargs.get(
                "folder", 
                "./data/GD/2024-JULY/maps/raw/geojson/combined"
            )
        self.load_map_file()

    def load_map_file(self):
        file_path = self.folder + "/" + self.admin_level + ".json"
        file_path = file_path.replace("//", "/")
        self.file_path = file_path
        self.content = json.load(open(file_path, "r"))

    def get_components(self): 
        items = self.content
        components = {} 
        
        for item in items: 
            if "geometry" not in item or item["geometry"] is None: 
                continue
            
            components[item["id"]] = \
                item["properties"]
            
            type_ = item["geometry"]["type"]

            if type_ == "Polygon":
                components[item["id"]]["polygons"] = \
                    [self.flatten_polygons(item["geometry"]["coordinates"])]
            elif type_ == "MultiPolygon": 
                components[item["id"]]["polygons"] = \
                    self.flatten_polygons(item["geometry"]["coordinates"])


        return components

    