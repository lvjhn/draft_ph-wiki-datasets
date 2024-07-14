import core.helpers as helpers
from core.main_article import MainArticle
import re

DEBUG = helpers.DEBUG

class ProvinceArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)  

    def extract_all(self): 
        return {
            "Coordinates" : self.extract_coordinates(),
            "Region" : self.extract_region(),
            "Founded" : self.extract_founded(),
            "Capital" : self.extract_capital(),
            "Largest City" : self.extract_largest_city(),
            "Government" : self.extract_government(),
            "Area" : self.extract_area(),
            "Elevation" : self.extract_elevation(),
            "Population" : self.extract_population(),
            "Divisions" : self.extract_divisions(),
            "Time Zone" : self.extract_time_zone(),
            "IDD Area Code" : self.extract_idd_area_code(),
            "Spoken Languages" : self.extract_spoken_languages(),
            "Website" : self.extract_website()
        }

    def extract_coordinates(self):
        DEBUG and print("@ Extracting coordinates.")
        
        latitude = \
            self.infobox.select(".latitude")[0].get_text() 
        longitude = \
            self.infobox.select(".longitude")[0].get_text()
        
        coords = {
            "Latitude" : latitude.strip(), 
            "Longitude" : longitude.strip()
        }
        
        return coords

    def extract_region(self):
        DEBUG and print("@ Extracting region.")
        
        return self.extractor.extract_pair(
            "Region"
        )
    
    def extract_founded(self):
        DEBUG and print("@ Extracting founded.")
        
        return self.extractor.extract_pair(
            "Founded"
        )
    
    def extract_capital(self):
        DEBUG and print("@ Extracting capital.")
        
        return self.extractor.extract_pair(
            "Capital",
            select=lambda y: y.select("a")[0].get_text()
        )
    
    def extract_largest_city(self):
        DEBUG and print("@ Extracting largest city.")
        
        return self.extractor.extract_pair(
            "Largest city",
            select=lambda y: y.select("a")[0].get_text()
        )
    
    def extract_government(self):
        DEBUG and print("@ Extracting government.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            y_n = self.Extractor.all_or_null(
                "(.*)\((.*)\)", y.get_text()
            )

            if y_n is None: 
                return (x, y.get_text)
         
            if len(y) > 0:
                y = {
                    "Name" : y_n[0][0], 
                    "Party" : y_n[0][1]
                }

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Government",
                select=extract
            )
        )
    
    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Total": 
                y = self.Extractor.to_float(
                    y.get_text().split(" ")[0]
                )

            elif x == "Rank": 
                y = self.Extractor.to_int(
                    self.Extractor.first_or_null(
                        "(.*)th out of .*",
                        y.get_text()
                    )
                )
            
            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Area",
                select=extract
            )
        )
    
    def extract_elevation(self):
        DEBUG and print("@ Extracting elevation.")
        
        # get name of body
        body = self.extractor.select_filtered(
            "th",
            filter_=
                lambda x, h, t: 
                    "Highest\xa0elevation" in t
        )
        body = self.Extractor.first_or_null(
            "\((.*)\)", 
            body.get_text()
        )

        # get highest elevation
        peak = self.extractor.extract_pair(
            "Highest\xa0elevation",
            select=
                lambda y: 
                    self.Extractor.to_float(
                        y.get_text().split(" ")[0].replace("\xa0m", "")
                    )
        )        

        highest_elevation = {
            "Body" : body, 
            "Peak" : peak
        }

        return highest_elevation
    
    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Total": 
                y = self.Extractor.to_int(
                    y.get_text()
                )

            elif x == "Density": 
                y = self.Extractor.to_float(
                    y.get_text().replace("/km2", "")
                )
           
            
            pair = (x, y)

            return pair

        population = dict(
            self.extractor.extract_pairs_from_partition(
                "Population",
                select=extract
            )
        )

        del population["Rank"]
        del population[""]

        return population
    
    def extract_divisions(self):
        DEBUG and print("@ Extracting divisions.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Independentcities": 
                x = "Independent cities"
                y = self.Extractor.to_int(y.get_text())

            elif x == "Component cities": 
                y = self.Extractor.to_int(y.get_text())

            elif x == "Municipalities": 
                y = self.Extractor.to_int(y.get_text())
            
            elif x == "Barangays": 
                y = self.Extractor.to_int(y.get_text())

            elif x == "Districts": 
                y = y.select("a")[0].get_text()

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Divisions",
                select=extract
            )
        )
    
    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        
        return self.extractor.extract_pair(
            "Time zone",
            select=lambda y: y.select("a")[0].get_text()
        )
    
    def extract_idd_area_code(self):
        DEBUG and print("@ Extracting IDD area code.")
        
        return self.extractor.extract_pair(
            "IDD",
            select=lambda y: y.get_text()
        )
    
    def extract_spoken_languages(self):
        DEBUG and print("@ Extracting spoken languages.")
        
        return self.extractor.extract_pair(
            "ISO 3166 code",
            select=lambda y: y.get_text()
        )
    
    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        
        return self.extractor.extract_pair(
            "Website",
            select=lambda y: y.get_text()
        )
    