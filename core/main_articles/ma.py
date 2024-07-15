import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class MunicipalityArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)

    def extract_all(self):
        return {
            "Coordinates" : self.extract_coordinates(),
            "Region" : self.extract_region(),
            "Province" : self.extract_province(),
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

    def extract_province(self):
        DEBUG and print("@ Extracting coordinates.")
        
        return self.extractor.extract_pair(
            "Province"
        )

    def extract_district(self):
        DEBUG and print("@ Extracting district.")
        
        return self.extractor.extract_pair(
            "District",
            select=
                lambda y: 
                    y.get_text().split(" ")[1].strip()[:-2]
        )



    def extract_founded(self):
        DEBUG and print("@ Extracting founded.")
        
        def extract(y):
            yd = self.Extractor.all_or_null(
                "([0-9]+) \(([a-zA-Z]*)\)",
                y.get_text()
            )

            if yd is None: 
                yd = self.Extractor.normalize( 
                    y.get_text(),
                    remove_brackets=True
                )
            else:    
                yd = dict(yd)

            return y

        return self.extractor.extract_pair(
            "Founded",
            select=extract
        )

    def extract_barangays(self):
        DEBUG and print("@ Extracting barangays.")
        
        return self.extractor.extract_pair(
            "Barangays",
            select=
                lambda y: 
                    self.Extractor.to_int(
                        y.get_text()
                    )
        )

    def extract_government(self):
        DEBUG and print("@ Extracting government.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Municipal Council": 
                y = [y.get_text() for y in y.select("li")]
                return (x, y)

            y_n = self.Extractor.all_or_null(
                "(.*)\((.*)\)", y.get_text()
            )

            if y_n is None: 
                return (x, y.get_text())
         
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
                return (x, y)

            elif x == "Independent component city":
                y = self.Extractor.to_float(
                    y.get_text().split(" ")[0]  
                ) 
                return (x, y)

            y = y.get_text()

            return (x, y)

        return (
            self.extractor.extract_pairs_from_partition(
                "Area",
                select=extract
            )
        )

    def extract_elevation(self):
        DEBUG and print("@ Extracting elevation.")
        
        return self.Extractor.to_int(
            self.extractor.extract_pair("Elevation")\
                .split(" ")[0]
        )

    def extract_highest_elevation(self): 
        DEBUG and print("@ Extracting highest elevation.")

        return self.Extractor.to_int(
            self.extractor.extract_pair("Highest\xa0elevation")\
                .split(" ")[0]
        )

    def extract_lowest_elevation(self): 
        DEBUG and print("@ Extracting lowest elevation.")

        return self.Extractor.to_int(
            self.extractor.extract_pair("Lowest\xa0elevation")\
                .split(" ")[0]
        )

    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Total":
                y = self.Extractor.to_int(y.get_text())
                return (x, y)

            elif x == "Density":
                y = self.Extractor.to_float(y.get_text().split("/km2")[0])
                return (x, y)

            elif x == "Households":
                y = self.Extractor.to_int(y.get_text())
                return (x, y)

            y = y.get_text()

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Population",
                select=extract
            )
        )

    def extract_economy(self):
        DEBUG and print("@ Extracting economy.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            
            if x == "Income class":
                y = y.get_text()
                return (x, y)

            elif x == "Poverty incidence":
                y = self.Extractor.deperc(
                    y.get_text().split(" ")[0]
                )
                return (x, y)

            elif x == "Revenue":
                y = " ".join([
                    y 
                    for y in y.get_text().split(" ")[0:2]
                    if y != ""
                ])[2:]
                print(y)
                y = self.Extractor.scale_item(y)
                return (x, y)

            elif x == "Assets":
                y = y.get_text().split(" ")
                first = y[0].split("\u200a")[1]
                scale = y[1]
                y = first + " " + scale
                y = self.Extractor.scale_item(y)
                return (x, y)

            elif x == "Expenditure":
                y = y.get_text().split(" ")
                first = y[0].split("\u200a")[1]
                scale = y[1]
                y = first + " " + scale
                y = self.Extractor.scale_item(y)
                return (x, y)

            elif x == "Liabilities":
                y = y.get_text().split(" ")
                first = y[0].split("\u200a")[1]
                scale = y[1]
                y = first + " " + scale
                y = self.Extractor.scale_item(y)
                return (x, y)

            y = y.get_text()

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Economy",
                select=extract
            )
        )

    def extract_service_provider(self):
        DEBUG and print("@ Extracting service provider.")
        
        def extract(x, y, i): 
            x = self.Extractor.remove_dot(x.get_text())
            y = y.get_text()

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition( 
                "Service provider",
                select=extract
            )
        )

    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        
        return self.extractor.extract_pair( 
            "Time zone"
        )

    def extract_zip_code(self):
        DEBUG and print("@ Extracting zip code.")
        
        return self.extractor.extract_pair( 
            "ZIP code"
        )

    def extract_psgc(self):
        DEBUG and print("@ Extracting PSGC.")
        
        return self.extractor.extract_pair( 
            "PSGC"
        )

    def extract_idd_area_code(self):
        DEBUG and print("@ Extracting IDD area code.")
        
        return self.extractor.extract_pair( 
            "IDD"
        )

    def extract_native_languages(self):
        DEBUG and print("@ Extracting native languages.")
        
        def extract(y): 
            y = str(y) 
            y = y.split("<br/>")
            y[0] = y[0].split(">")[1]
            y[1] = y[1].split("<")[0]
            return y

        return self.extractor.extract_pair( 
            "Native languages",
            select=extract
        )

    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        
        return self.extractor.extract_pair( 
            "Website"
        )