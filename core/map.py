import core.helpers as helpers
from shapely \
    import MultiPolygon, GeometryCollection, LineString, Polygon, \
           union_all, make_valid, STRtree, envelope
import svgwrite       
import numpy as np

class Map:
    def __init__(self, *args, **kwargs):
        self.cache = kwargs.get("cache", True)
        self.should_preload = kwargs.get("preload", True)

        if self.should_preload: 
            self.preload
    
    # Source: https://realpython.com/python-flatten-list/
    def flatten_extend(self, matrix):
        flat_list = []
        for row in matrix:  
            flat_list.extend(row)
        return flat_list

    def flatten_polygons(self, polygons):
        for i in range(len(polygons)):
            if hasattr(polygons[i], "tolist"):
                polygons[i] = polygons[i].tolist()
        polygons = self.flatten_extend(polygons)
        return polygons

    def ordered_pair(self, pair): 
        class Float: 
            def __init__(self, a):
                self.a = a

            def __eq__(self, b): 
                return self.a == self.b 

    def envelope_intersects(self, env1, env2):
        """
        Checks for intersection between two Shapely geometries using envelopes.

        Args:
            geom1: The first Shapely geometry object.
            geom2: The second Shapely geometry object.

        Returns:
            True if the envelopes of the geometries intersect, False otherwise.
        """

        min_x = 0
        min_y = 1
        max_x = 2
        max_y = 3
        

        # Check for non-intersection conditions (early termination)
        if env1[max_x] < env2[min_x] or env1[min_x] > env2[max_x] or \
            env1[max_y] < env2[min_y] or env1[min_y] > env2[max_y]:
            return False

        # Envelopes intersect, potential full geometry intersection needed
        return True

    def adjacency_list(self): 
        components = self.get_components() 

        locations = {} 
        bboxes = {}
        adjacencies = {}

        i = 0
        n = len(components)
        for key in components: 
            print(f"@ Gathering vertices {i + 1} of {n}                ", end="\r")
            component = components[key]
            polygons = component["polygons"]
            locations[key] = \
                GeometryCollection([Polygon(polygon) for polygon in  polygons])
            locations[key] = \
                make_valid(MultiPolygon(locations[key]))

            bboxes[key] = \
                locations[key].bounds

            if key not in adjacencies:
                adjacencies[key] = dict()
            i += 1

        i = 0

        intersections = 0 
        non_intersections = 0

        tree = STRtree(list(locations.values()))
        keys = list(locations.keys())

        i = 0
        for key_a in locations: 
            print(f"@ Finding adjacencies {i + 1} of {n}                   ", end="\r")
            candidate_neighbors = tree.query(locations[key_a])
            candidate_neighbors = [keys[i] for i in candidate_neighbors]

            for key_b in candidate_neighbors: 
                bbox_a = bboxes[key_a]
                bbox_b = bboxes[key_b]
                if self.envelope_intersects(bbox_a, bbox_b):
                    intersections += 1
                    if key_a == key_b:
                        continue
                    if locations[key_a].intersects(locations[key_b]):
                        adjacencies[key_a][key_b] = 0
                        intersection = \
                            locations[key_a].intersection(locations[key_b])
                        adjacencies[key_a][key_b] = intersection.length


                else: 
                    non_intersections += 1
                
            i += 1

        return adjacencies
                
    def preload(self): 
        self.components = self.get_components() 
    
    def draw_svg(self, outfile, id_field="id", **kwargs): 
        dw = \
            svgwrite.Drawing(outfile, **kwargs)

        components = self.components 

        for component in components.values():
            polygons = component["polygons"]
            id_ = str(component[id_field]).replace(" ", "_")
            for polygon in polygons:
                dw.add(
                    dw.polygon(
                        polygon, 
                        id=id_
                    )
                )

        dw.save()
    