import core.helpers as helpers
from core.main_article import MainArticle

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
        pass

    def extract_region(self):
        DEBUG and print("@ Extracting region.")
        pass
    
    def extract_founded(self):
        DEBUG and print("@ Extracting founded.")
        pass
    
    def extract_capital(self):
        DEBUG and print("@ Extracting capital.")
        pass
    
    def extract_largest_city(self):
        DEBUG and print("@ Extracting largest city.")
        pass
    
    def extract_government(self):
        DEBUG and print("@ Extracting government.")
        pass
    
    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        pass
    
    def extract_elevation(self):
        DEBUG and print("@ Extracting elevation.")
        pass
    
    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        pass
    
    def extract_divisions(self):
        DEBUG and print("@ Extracting divisions.")
        pass
    
    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        pass
    
    def extract_idd_area_code(self):
        DEBUG and print("@ Extracting IDD area code.")
        pass
    
    def extract_spoken_languages(self):
        DEBUG and print("@ Extracting spoken languages.")
        pass
    
    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        pass
    