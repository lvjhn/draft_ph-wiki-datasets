import core.helpers as helpers

class Map:
    def __init__(self, *args, **kwargs):
        self.cache = kwargs.get("cache", True)
        self.should_preload = kwargs.get("preload", True)

        if self.should_preload: 
            self.preload

    def union_by_attribute(self): 
        pass 

    def union_by_attributes(self):
        pass 

    def components(self): 
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

    def to_svg(self): 
        pass 

    

    