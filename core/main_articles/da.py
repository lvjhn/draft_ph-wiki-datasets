import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class DistrictArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self,article, *args, **kwargs)

    def extract_all(self): 
        return {
            "Province" : self.extract_province(),
            "Region" : self.extract_region(),
            "Population (2020)" : self.extract_population(),
            "Electorate" : self.extract_electorate(),
            "Major Settlements" : self.extract_major_settlements(),
            "Area" : self.extract_area(),
            "Created" : self.extract_created(),
            "Extract Representative" : self.extract_representative(),
            "Political Party" : self.extract_political_party(),
            "Congressional Bloc" : self.extract_congressional_bloc(),
            "Constituent LGUs History" : self.extract_clgus_history()
        }

    def extract_province(self):
        DEBUG and print("@ Extracting province.")

        try:
            return self.extractor.extract_pair(
                "Province"
            )
        except: 
            return None

    def extract_region(self):
        DEBUG and print("@ Extracting region.")
        
        try:
            return self.extractor.extract_pair(
                "Region"
            )
        except: 
            return None

    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        
        def extract(y): 
            y = y.get_text() 
            y = self.Extractor.all_or_null("(.*) \((.*)\)", y)[0]
            
            no = self.Extractor.to_int(y[0])
            year = self.Extractor.to_int(y[1])
            
            y = {
                "No." : no, 
                "Year" : year
            }

            return y

        try:
            return self.extractor.extract_pair(
                "Population", 
                select=extract
            )
        except:
            return {
                "No." : None, 
                "Year" : None
            }

    def extract_electorate(self):
        DEBUG and print("@ Extracting electorate.")
        
        def extract(y): 
            y = y.get_text() 
            y = self.Extractor.all_or_null("(.*) \((.*)\)", y)[0]
            
            no = self.Extractor.to_int(y[0])
            year = self.Extractor.to_int(y[1])
            
            y = {
                "No." : no, 
                "Year" : year
            }

            return y

        try:
            return self.extractor.extract_pair(
                "Electorate", 
                select=extract
            )
        except: 
            return {
                "No." : None, 
                "Year" : None
            }
    
    def extract_major_settlements(self):
        DEBUG and print("@ Extracting major settlements.")
        
        try: 
            quantity = self.extractor.extract_pair(
                "settlements", 
                select=
                    lambda y: 
                        self.Extractor.to_int(
                            self.Extractor.first_or_null(
                                "([0-9]+) LGUs",
                                y.get_text()
                            )
                        )
                    
            ) 

            lgus = self.extractor.extract_pair(
                "settlements", 
                select=
                    lambda y: 
                        [x.get_text() for x in y.select("a")[1:]]
            ) 

            y = {
                "Quantity" : quantity,
                "LGUs" : lgus
            }
        except: 
            return {
                "Quantity" : None,
                "LGUs" : None
            }

       
    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        try:
            return self.extractor.extract_pair(
                "Area", 
                select=
                    lambda y:
                        self.Extractor.to_float(
                            y.get_text().split("\xa0km2")[0]
                        )
            )
        except: 
            return None
        
    def extract_created(self):
        DEBUG and print("@ Extracting created.")
        try:
            return self.extractor.extract_pair(
                "Created", 
                select=
                    lambda y:
                        self.Extractor.to_int(y.get_text())
            )
        except:
            return None
    
    def extract_representative(self):
        DEBUG and print("@ Extracting representative.")
        try:
            return self.extractor.extract_pair(
                "Representative"
            )
        except:
            return None
    
    def extract_political_party(self):
        DEBUG and print("@ Extracting political party.")
        try: 
            return self.extractor.extract_pair(
                "Political party"
            )
        except: 
            return None
    
    def extract_congressional_bloc(self):
        DEBUG and print("@ Extracting congressional bloc.")
        try:
            return self.extractor.extract_pair(
                "Congressional bloc"
            )
        except:
            return None

    def extract_clgus_history(self):
        DEBUG and print("@ Extracting CLGUs history.")
        
        try:
            items = self.extractor.extract_column(
                "table",
                9,
                filter_=self.extractor.from_headers([
                    "Image",
                    "Member",
                    "Term of office",
                    "Congress",
                    "Party",
                    "Constituent LGU"
                ])
            )

            items = [item.split(" ") for item in items]
            items = [tuple([item[0], item[1:]]) for item in items]
            items = dict(items)
            
            return items
        except: 
            return None
            