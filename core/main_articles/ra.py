import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class RegionArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(article, *args, **kwargs)

    def extract_all(self):
        return {
            "Coordinates" : self.extract_coordinates(),
            "Country" : self.extract_country(),
            "Island Group" : self.extract_island_group(),
            "Regional Center" : self.extract_regional_center(),
            "Area" : self.extract_area(),
            "Highest Elevation" : self.extract_highest_elevation(),
            "Population" : self.extract_population(),
            "Time Zone" : self.extract_time_zone(),
            "ISO 3166 Code" : self.extract_iso_3166_code(),
            "Provinces" : self.extract_provinces(),
            "Independent Cities" : self.extract_independent_cities(),
            "Component Cities" : self.extract_component_cities(),
            "Muncipalities" : self.extract_municipalities(),
            "Barangays" : self.extract_barangays(),
            "Congressional Districts" : self.extract_congressional_districts(),
            "Extract Languages" : self.extract_languages(),
            "GDP" : self.extract_gdp(),
            "Growth Rate" : self.extract_growth_rate(),
            "HDI" : self.extract_hdi(),
            "HDI Rank" : self.extract_hdi_rank(),
            "Website" : self.extract_website()
        } 

    def extract_coordinates(self):
        DEBUG and print("@ Extracting coordinates.")
        pass

    def extract_country(self):
        DEBUG and print("@ Extracting country.")
        pass

    def extract_island_group(self):
        DEBUG and print("@ Extracting island group.")
        pass

    def extract_regional_center(self):
        DEBUG and print("@ Extracting regional center.")
        pass
    
    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        pass
    
    def extract_highest_elevation(self):
        DEBUG and print("@ Extracting highest elevation.")
        pass
    
    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        pass
    
    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        pass
    
    def extract_iso_3166_code(self):
        DEBUG and print("@ Extracting 3166 code.")
        pass
    
    def extract_provinces(self):
        DEBUG and print("@ Extracting provinces.")
        pass

    def extract_independent_cities(self):
        DEBUG and print("@ Extracting independent cities.")
        pass

    def extract_component_cities(self):
        DEBUG and print("@ Extracting component cities.")
        pass
    
    def extract_municipalities(self):
        DEBUG and print("@ Extracting municipalities.")
        pass
    
    def extract_barangays(self):
        DEBUG and print("@ Extracting barangays.")
        pass
    
    def extract_congressional_districts(self):
        DEBUG and print("@ Extracting congressional districts.")
        pass
    
    def extract_languages(self):
        DEBUG and print("@ Extracting languages.")
        pass
    
    def extract_gdp(self):
        DEBUG and print("@ Extracting GDP.")
        pass
    
    def extract_growth_rate(v):
        DEBUG and print("@ Extracting growth rate.")
        pass
    
    def extract_hdi(self):
        DEBUG and print("@ Extracting HDI.")
        pass
    
    def extract_hdi_rank(self):
        DEBUG and print("@ Extracting HDI rank.")
        pass
    
    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        pass
      

    
