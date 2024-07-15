import core.helpers as helpers
from core.main_article import MainArticle
import re

DEBUG = helpers.DEBUG

class RegionArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)

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
        
        latitude = \
            self.infobox.select(".latitude")[0].get_text() 
        longitude = \
            self.infobox.select(".longitude")[0].get_text()
        
        coords = {
            "Latitude" : latitude.strip(), 
            "Longitude" : longitude.strip()
        }
        
        return coords

    def extract_country(self):
        DEBUG and print("@ Extracting country.")
        
        country = self.extractor.extract_pair(
            "Country",
            base=self.infobox
        )
        
        return country.strip()

    def extract_island_group(self):
        DEBUG and print("@ Extracting island group.")
        
        island_group = self.extractor.extract_pair(
            "Island",
            base=self.infobox
        )
        
        return island_group.strip()

    def extract_regional_center(self):
        DEBUG and print("@ Extracting regional center.")
        
        regional_center = self.extractor.extract_pair(
            "Regional center",
            base=self.infobox
        )

        return regional_center.strip()
    
    def extract_area(self):
        DEBUG and print("@ Extracting area.")

        def extract(x, y, i):
            x = x.get_text().replace("\xa0•\xa0", "")
            y = y.get_text()

            if x == "Total": 
                y = y.split(" ")[0].replace("\xa0km2", "")
                y = self.Extractor.to_float(y)

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Area",
                select=extract
            )
        )
    
    def extract_highest_elevation(self):
        DEBUG and print("@ Extracting highest elevation.")
        
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
                    y.get_text().split(" ")[0]
        )        

        highest_elevation = {
            "Body" : body, 
            "Peak" : peak
        }

        return highest_elevation
    
    def extract_population(self):
        DEBUG and print("@ Extracting population.")
        
        def extract(x, y, i):
            x = x.get_text().replace("\xa0•\xa0", "")
            y = y.get_text()

            if x == "Total":
                y = self.Extractor.to_int(y) 
            
            elif x == "Density": 
                y = y.split(" ")
                y = y[0]
                y = y.replace("/km2", "")
                y = self.Extractor.to_float(y)

            pair = (x, y)

            return pair

        return dict(
            self.extractor.extract_pairs_from_partition(
                "Population",
                select=extract
            )
        ) 
    
    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        return self.extractor.extract_pair(
            "Time zone"
        )
    
    def extract_iso_3166_code(self):
        DEBUG and print("@ Extracting 3166 code.")
        return self.extractor.extract_pair(
            "ISO 3166 code"
        )
    
    def extract_provinces(self):
        DEBUG and print("@ Extracting provinces.")
        
        def extract(y): 
            text = y.get_text().strip()
            tokens = text.split("\n")
           
            n_provinces = int(tokens[0]) 
            provinces = [y for y in tokens[1:]]

            pair = {
                "Provinces (Count)" :  n_provinces, 
                "Provinces" : provinces
            }

            return pair

        return self.extractor.extract_pair(
            "Provinces",
            select=extract,
            base=self.infobox
        )
         

    def extract_independent_cities(self):
        DEBUG and print("@ Extracting independent cities.")
        
        def extract(y): 
            text = y.get_text().strip()
            tokens = text.split("\n")
           
            n_independent_cities = int(tokens[0]) 
            independent_cities = [y for y in tokens[1:]]

            pair = {
                "Independent Cities (Count)" :  n_independent_cities, 
                "Independent Cities" : independent_cities
            }

            return pair

        return self.extractor.extract_pair(
            "Independent cities",
            select=extract,
            base=self.infobox
        )

    def extract_component_cities(self):
        DEBUG and print("@ Extracting component cities.")
        
        def extract(y): 
            text = y.get_text().strip()
            tokens = text.split("\n")
           
            n_component_cities = int(tokens[0]) 
            component_cities = [y for y in tokens[1:]]

            pair = {
                "Component Cities (Count)" :  n_component_cities, 
                "Component Cities" : component_cities
            }

            return pair

        return self.extractor.extract_pair(
            "Component cities",
            select=extract,
            base=self.infobox
        )   
    
    def extract_municipalities(self):
        DEBUG and print("@ Extracting municipalities.")
        return self.extractor.extract_pair(
            "Municipalities",
            base=self.infobox
        )   
    
    def extract_barangays(self):
        DEBUG and print("@ Extracting barangays.")
        return self.extractor.extract_pair(
            "Barangays",
            select=
                lambda y:   
                    self.Extractor.to_int(y.get_text()),
            base=self.infobox
        )   
    
    def extract_congressional_districts(self):
        DEBUG and print("@ Extracting congressional districts.")
        return self.extractor.extract_pair(
            "Barangays",
            select=
                lambda y:   
                    self.Extractor.to_int(y.get_text()),
            base=self.infobox
        )   
    
    def extract_languages(self):
        DEBUG and print("@ Extracting languages.")

        def extract(y):
            first_level = \
                y.select(".plainlist > ul")[0]\
                 .findChildren("li", recursive=False) 

            languages = {}
            for first_level_el in first_level: 
                
                # get first level language
                language = first_level_el.find("a").get_text()
                hlist = first_level_el.select(".hlist")
                languages[language] = {}

                # check if has sublanguages
                if len(hlist) > 0: 
                    hlist = hlist[0]
                else: 
                    continue 

                items = [
                    li.get_text().replace("(", "").replace(")", "")
                    for li in hlist.select("li")
                ]
                languages[language] = items

            return languages

        return self.extractor.extract_pair(
            "Languages",
            select=extract,
            base=self.infobox
        )    
    
    
    def extract_gdp(self):
        DEBUG and print("@ Extracting GDP.")

        def extract(y): 
            y = y.get_text()
            peso = (y.split("$")[0][1:]).strip()
            peso = self.Extractor.scale_item(peso)

            return peso

        return self.extractor.extract_pair(
            "GDP",
            select=extract,
            base=self.infobox
        )
    
    def extract_growth_rate(self):
        DEBUG and print("@ Extracting growth rate.")
        
        def extract(y):

            # get trend
            trend = 0

            if len(y.select("[title='Increase']")) > 0:
                trend = 1
            elif len(y.select("[title='Decrease']")) > 0:
                trend = -1

            # get percentage 
            perc = self.Extractor.first_or_null(
                "\((.*)%\)",
                y.get_text()
            )

            y = {
                "Trend" : trend, 
                "Percentage" : perc
            }

            return y

        return self.extractor.extract_pair(
            "Growth rate", 
            select=extract,
            base=self.infobox
        )
        
    
    def extract_hdi(self):
        DEBUG and print("@ Extracting HDI.")
        
        def extract(y):

            # get trend
            trend = 0

            if len(y.select("[title='Increase']")) > 0:
                trend = 1
            elif len(y.select("[title='Decrease']")) > 0:
                trend = -1

            # get percentage 
            perc = self.Extractor.first_or_null(
                "(.*)\s\(",
                y.get_text()
            )

            y = {
                "Trend" : trend, 
                "Percentage" : perc
            }

            return y

        return self.extractor.extract_pair(
            "HDI", 
            select=extract,
            base=self.infobox
        )
        
    
    def extract_hdi_rank(self):
        DEBUG and print("@ Extracting HDI rank.")
        
        def extract(y): 
            rank = \
                self.Extractor.first_or_null(
                    "([0-9]+).?.? in the Philippines",
                    y.get_text()
                )
            year = \
                self.Extractor.first_or_null(
                    "\((.*)\)", 
                    y.get_text()
                )

            y = {
                "Rank" : rank, 
                "Year" : year
            }

            return y 

        return self.extractor.extract_pair(
            "HDI rank",
            select=extract,
            base=self.infobox
        )
    
    def extract_website(self):
        DEBUG and print("@ Extracting website.")
        
        return self.extractor.extract_pair(
            "Website",
            base=self.infobox
        )
      

    
