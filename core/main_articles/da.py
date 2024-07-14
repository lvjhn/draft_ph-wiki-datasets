import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class DistrictArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)

    def extract_all(self): 
        return {
            "Coordinates" : self.extract_coordinates(),
            "Province" : self.extract_province(),
            "Region" : self.extract_region(),
            "Population" : self.extract_population(),
            "Electorate" : self.extract_electorate(),
            "Major Settlements" : self.extract_major_settlements(),
            "Area" : self.extract_area(),
            "Created" : self.extract_created(),
            "Extract Representative" : self.extract_representative(),
            "Political Party" : self.extract_political_party(),
            "Congressional Bloc" : self.extract_congressional_bloc(),
            "Constituent LGUs History" : self.extract_clgus_history()
        }

    def extract_coordinates(self):
        DEBUG and print("@ Extracting coordinates.")
        pass

    def extract_province(self):
        DEBUG and print("@ Extracting province.")
        pass

    def extract_region(self):
        DEBUG and print("@ Extracting region.")
        pass

    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        pass

    def extract_electorate(self):
        DEBUG and print("@ Extracting electorate.")
        pass
    
    def extract_major_settlements(self):
        DEBUG and print("@ Extracting major settlements.")
        pass
    
    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        pass
    
    def extract_created(self):
        DEBUG and print("@ Extracting created.")
        pass
    
    def extract_representative(self):
        DEBUG and print("@ Extracting representative.")
        pass
    
    def extract_political_party(self):
        DEBUG and print("@ Extracting political party.")
        pass
    
    def extract_congressional_bloc(self):
        DEBUG and print("@ Extracting congressional block.")
        pass

    def extract_clgus_history(self):
        DEBUG and print("@ Extracting CLGUs history.")
        pass
    