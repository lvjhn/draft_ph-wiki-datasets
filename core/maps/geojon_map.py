import core.helpers as helpers

from core.map import Map

class GeoJSONMap(Map):
    def __init__(self, *args, **kwargs):
        Map.__init__(self, *args, **kwargs)
        self.admin_level = kwargs.get("admin_level", "regions")

    def components(self): 
        pass 

    def union_by_attribute(self): 
        pass 

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
    

    