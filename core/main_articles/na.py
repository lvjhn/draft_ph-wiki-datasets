import core.helpers as helpers
from core.main_article import MainArticle
import re

DEBUG = helpers.DEBUG

class NationalArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)
        self.infobox = self.extractor._.select(".infobox")[0]

    def extract_all(self):
        return {
            "capital" : self.extract_capital(), 
            "regional_languages" : self.extract_regional_languages(), 
            "sign_languages" : self.extract_sign_languages(), 
            "other_languages" : self.extract_other_languages(), 
            "ethnic_groups" : self.extract_ethnic_groups(), 
            "religions" : self.extract_religions(), 
            "demonyms" : self.extract_demonyms(), 
            "government" : self.extract_government(),
            "president" : self.extract_president(), 
            "vice_president" : self.extract_vice_president(),
            "senate_president" : self.extract_senate_president(),
            "house_speaker" : self.extract_house_speaker(),
            "chief_justice" : self.extract_chief_justice(),
            "legislature" : self.extract_legislature(), 
            "lower_house" : self.extract_lower_house(), 
            "upper_house" : self.extract_upper_house(), 
            "independence" : self.extract_independence(),
            "area" : self.extract_area(),
            "population" : self.extract_population(),
            "gdp_ppp" : self.extract_gdp_ppp(),
            "gdp_nominal" : self.extract_gdp_nominal(),
            "gini" : self.extract_gini(),
            "hdi" : self.extract_hdi(),
            "currency" : self.extract_currency(),
            "time_zone" : self.extract_time_zone(),
            "date_format" : self.extract_date_format(),
            "driving_side" : self.extract_driving_side(),
            "calling_code" : self.extract_calling_code(),
            "iso_3166_code" : self.extract_iso_3166_code()
        }

    def extracct_capital(self):
        DEBUG and print("@ Extracting capital.")
        return self.extractor.extract_pair(
            "Capital",
            select=lambda x: list(filter(lambda x: x != "", [
                self.Extractor.normalize(x.get_text(), remove_brackets=True)
                for x in x.select("a") 
            ])),
            base=self.infobox
        )

    def extract_capital(self):
        DEBUG and print("@ Extracting capital.")
        return self.extractor.extract_pair(
            "Capital",
            select=lambda x: list(filter(lambda x: x != "", [
                self.Extractor.normalize(x.get_text(), remove_brackets=True)
                for x in x.select("a") 
            ])),
            base=self.infobox
        )
        
    def extract_largest_city(self):
        DEBUG and print("@ Extracting largest city.")
        return self.extractor.extract_pair(
            "Largest city",
            base=self.infobox
        )

    def extract_official_languages(self):
        DEBUG and print("@ Extracting official languages.")
        return self.extractor.extract_pair(
            "Official\xa0language", 
            select=lambda x: list(filter(lambda x: x != "", [
                self.Extractor.normalize(x.get_text(), remove_brackets=True)
                for x in x.select("a") 
            ])),
            base=self.infobox
        )

    def extract_regional_languages(self):
        DEBUG and print("@ Extracting regional languages.")
        return self.extractor.extract_pair(
            "Recognized regional\xa0languages",
            select=lambda x: self.Extractor.to_int(
                self.Extractor.normalize(
                    x.get_text(),
                    remove_brackets=True
                )
            ),
            base=self.infobox
        )

    def extract_sign_languages(self):
        DEBUG and print("@ Extracting sign languages.")
        return self.extractor.extract_pair(
            "National sign language",
            base=self.infobox
        )

    def extract_other_languages(self):
        DEBUG and print("@ Extracting other languages.")
        return self.extractor.extract_pair(
            "Other recognized languages", 
            select=lambda x: list(filter(lambda x: x != "", [
                self.Extractor.normalize(x.get_text(), remove_brackets=True)
                for x in x.select("a") 
            ])),
            base=self.infobox
        )

    def extract_ethnic_groups(self):
        DEBUG and print("@ Extracting ethnic groups.")
        def extract(x): 
            items = x.select("li")
            items = [
                x.get_text().split(" ") 
                for x in items if x is not None
            ]
            items = [
                (x[1], self.Extractor.to_float(x[0]))
                for x in items if x is not None
            ]
            return dict(items)

        return self.extractor.extract_pair(
            "Ethnic\xa0groups", 
            select=extract,
            base=self.infobox
        )

    def extract_religions(self):
        DEBUG and print("@ Extracting religions.")
        def extract(x): 
            items = x.select("ul")[0]\
                     .findChildren("li", recursive=False)
            for i in range(len(items)):
                items[i] = items[i].get_text() 
                items[i] = items[i].split("\n")
                items[i] = [x for x in items[i] if x != ""]
                items[i] = items[i][0]
                items[i] = items[i].split(" ")
                items[i] = (
                    items[i][1],
                    self.Extractor.deperc(items[i][0])
                )

            return dict(items)

        return self.extractor.extract_pair(
            "Religion", 
            select=extract,
            base=self.infobox
        )

    def extract_demonyms(self):
        DEBUG and print("@ Extracting demonyms.")
        def extract(x): 
            items = x.get_text()
            items = [x.strip() for x in items.split(")")]
            items = [tuple(x.split("(")) for x in items]
            items = [x for x in items if len(x) > 1]
            return dict(items)

        return self.extractor.extract_pair(
            "Demonym(s)", 
            select=extract,
            base=self.infobox
        )

    def extract_government(self):
        DEBUG and print("@ Extracting government.")
        return self.extractor.extract_pair(
            "Government",
            base=self.infobox
        )

    def extract_president(self):
        DEBUG and print("@ Extracting president.")
        return self.extractor.extract_pair(
            "President",
            base=self.infobox
        )

    def extract_vice_president(self):
        DEBUG and print("@ Extracting president.")
        return self.extractor.extract_pair(
            "Vice President",
            base=self.infobox
        )
        
    def extract_senate_president(self): 
        DEBUG and print("@ Extracting senate president.")
        return self.extractor.extract_pair(
            "Senate President",
            base=self.infobox
        )

    def extract_house_speaker(self): 
        DEBUG and print("@ Extracting house speaker.")
        return self.extractor.extract_pair(
            "House Speaker",
            base=self.infobox
        )

    def extract_chief_justice(self): 
        DEBUG and print("@ Extracting chief justice.")
        return self.extractor.extract_pair(
            "Chief Justice",
            base=self.infobox
        )

    def extract_legislature(self): 
        DEBUG and print("@ Extracting legislature.")
        return self.extractor.extract_pair(
            "Legislature",
            base=self.infobox
        )
    
    def extract_upper_house(self): 
        DEBUG and print("@ Extracting upper house.")
        return self.extractor.extract_pair(
            "Upper house",
            base=self.infobox
        ) 

    def extract_lower_house(self): 
        DEBUG and print("@ Extracting lower house.")
        return self.extractor.extract_pair(
            "Lower house",
            base=self.infobox
        )  

    def extract_independence(self): 
        DEBUG and print("@ Extracting independence declaration.")
        return dict(
            self.extractor.extract_pairs_from_partition(
                "Independence"
            ) 
        )

    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        return dict(
            self.extractor.extract_pairs_from_partition(
                "Area",
                select=lambda x, y, i: (
                    (
                        x.get_text()\
                            .replace("•\xa0", "")\
                            .replace("\xa0", "")\
                            .replace("(%)", "_perc")\
                            .lower(), 
                        self.Extractor.to_float(
                            re.split("\[.*\]", y.get_text())[0]
                        )
                    )
                )
            ) 
        )

    def extract_population(self):
        DEBUG and print("@ Extracting population.")

        def extract(x, y, i):
            # fix label
            x = x.get_text().replace("•\xa0", "") 
            x = x.replace("\xa0", "_") 

            # fix value
            y = self.Extractor.normalize(
                y.get_text(), 
                remove_brackets=True,
                remove_parentheses=True,
                trim=True
            )
            y = y.replace("/km2", "")
            y = y.replace("$", "")
            y = y.replace(",", "")
            
            if "." in y: 
                y = self.Extractor.to_float(y)
            else: 
                try:
                    y = self.Extractor.to_int(y)
                except:
                    pass 

            return (x, y)
            
            
        return dict(
            self.extractor.extract_pairs_from_partition(
                "Population",
                select=extract
            )
        ) 

    def extract_gdp_ppp(self):
        DEBUG and print("@ Extracting GDP (PPP).")
        
        def extract(x, y, i):
            # fix label
            x = x.get_text().replace("•\xa0", "") 
            x = x.replace("\xa0", "_") 

            # fix value
            y = self.Extractor.normalize(
                y.get_text(), 
                remove_brackets=True,
                remove_parentheses=True,
                trim=True
            )
            y = y.replace("/km2", "")
            y = y.replace("$", "")
            y = y.replace(",", "")
            y = self.Extractor.scale_words(y)

            return (x, y)
            
            
        return dict(
            self.extractor.extract_pairs_from_partition(
                "GDP\xa0(PPP)",
                select=extract
            )
        )  

    def extract_gdp_nominal(self):
        DEBUG and print("@ Extracting GDP (Nominal).")
        
        def extract(x, y, i):
            # fix label
            x = x.get_text().replace("•\xa0", "") 
            x = x.replace("\xa0", "_") 

            # fix value
            y = self.Extractor.normalize(
                y.get_text(), 
                remove_brackets=True,
                remove_parentheses=True,
                trim=True
            )
            y = y.replace("/km2", "")
            y = y.replace("$", "")
            y = y.replace(",", "")
            y = self.Extractor.scale_words(y)

            return (x, y)
            
            
        return dict(
            self.extractor.extract_pairs_from_partition(
                "GDP\xa0(nominal)",
                select=extract
            )
        )  

    def extract_gini(self):
        DEBUG and print("@ Extracting Gini.")
        return self.extractor.extract_pair(
            "Gini",
            select=lambda y: 
                ( 
                    self.Extractor.first_or_null(
                        r"\xa0([0-9]+.[0-9]+)",
                        str(y),
                    ),
                    self.Extractor.first_or_null(
                        r"medium|low|high",
                        str(y),
                    )
                )
        ) 

    def extract_hdi(self):
        DEBUG and print("@ Extracting HDI.")
        return self.extractor.extract_pair(
            "HDI",
            select=lambda y: 
                ( 
                    self.Extractor.first_or_null(
                        r"\xa0([0-9]+.[0-9]+)",
                        str(y),
                    ),
                    self.Extractor.first_or_null(
                        r"medium|low|high",
                        str(y),
                    )
                )
        ) 

    def extract_currency(self):
        DEBUG and print("@ Extracting currency.")
        return self.extractor.extract_pair(
            "Currency",
            select=lambda y: 
                self.Extractor.normalize(
                    y.get_text(), 
                    remove_brackets=True,
                    remove_parentheses=True,
                    title_case=True
                )
        )  

    def extract_time_zone(self):
        DEBUG and print("@ Extracting time zone.")
        return self.extractor.extract_pair(
            "Time zone"
        )  

    def extract_date_format(self):
        DEBUG and print("@ Extracting date format.")
        
        def extract(y):
            y = self.Extractor.first_or_null("\<td.*\>([DMY/-]*)\<sup", str(y))
            return y

        return self.extractor.extract_pair(
            "Date format",
            select=extract
        )  

    def extract_driving_side(self):
        DEBUG and print("@ Extracting driving side.")
        return self.extractor.extract_pair(
            "Driving side"
        )   

    def extract_calling_code(self):
        DEBUG and print("@ Extracting calling code.")
        return self.extractor.extract_pair(
            "Calling code"
        )    

    def extract_iso_3166_code(self):
        DEBUG and print("@ Extracting ISO 3166 code.")
        return self.extractor.extract_pair(
            "ISO 3166 code"
        )    
 



        