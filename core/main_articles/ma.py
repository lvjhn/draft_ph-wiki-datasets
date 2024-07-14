import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class MunicipalityArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(article, *args, **kwargs)

    def extract_all(self):
        return {
            "Coordinates" : self.extract_coordinates(),
            "Country" : self.extract_country(),
            "Region" : self.extract_region(),
            "District" : self.extract_district(),
            "Founded" : self.extract_founded(),
            "Barangays" : self.extract_barangays(),
            "Government" : self.extract_government(),
            "Area" : self.extract_area(),
            "Elevation" : self.extract_elevation(),
            "Highest Elevation" : self.extract_highest_elevation(),
            "Lowest Elevation" : self.extract_lowest_elevation(),
            "Population" : self.extract_population(),
            "Economy" : self.extract_economy(),
            "Service Provider" : self.extract_service_provider(),
            "Time Zone" : self.extract_time_zone(),
            "Zip Code" : self.extract_zip_code(),
            "PSGC" : self.extract_psgc(),
            "IDD Area Code" : self.extract_idd_area_code(),
            "Native Languages" : self.extract_native_languages(),
            "Website" : self.extract_website()
        }   

    def extract_coordinates(self):
        DEBUG and print("@ Extracting coordinates.")
        pass

    def extract_country(self):
        DEBUG and print("@ Extracting country.")
        pass

    def extract_region(self):
        DEBUG and print("@ Extracting region.")
        pass

    def extract_district(self):
        DEBUG and print("@ Extracting district.")
        pass

    def extract_founded(self):
        DEBUG and print("@ Extracting founded.")
        pass

    def extract_barangays(self):
        DEBUG and print("@ Extracting barangays.")
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

    def extract_highest_elevation(self):
        DEBUG and print("@ Extracting highest elevation.")
        pass

    def extract_lowest_elevation(self):
        DEBUG and print("@ Extracting lowest elevation.")
        pass

    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        pass

    def extract_economy(self):
        DEBUG and print("@ Extracting economy.")
        pass

    def extract_service_provider(self):
        DEBUG and print("@ Extracting service provider.")
        pass

    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        pass

    def extract_zip_code(self):
        DEBUG and print("@ Extracting zip code.")
        pass

    def extract_psgc(self):
        DEBUG and print("@ Extracting PSGC.")
        pass

    def extract_idd_area_code(self):
        DEBUG and print("@ Extracting IDD area code.")
        pass

    def extract_native_languages(self):
        DEBUG and print("@ Extracting native languages.")
        pass

    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        pass