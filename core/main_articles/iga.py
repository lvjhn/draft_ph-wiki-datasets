import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class IslandGroupArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)

    def extract_all(self):
        return {
            "Coordinates" : self.extract_coordinates(),
            "Adjacent To" : self.extract_adjacent_to(),
            "Major Islands" : self.extract_major_islands(),
            "Area" : self.extract_area(),
            "Rank" : self.extract_area_rank(),
            "Coastline" : self.extract_coastline(),
            "Highest Elevation" : self.extract_highest_elevation(),
            "Highest Point" : self.extract_highest_point(),
            "Regions" : self.extract_regions(),
            "Provinces" : self.extract_provinces(),
            "Largest Settlement" : self.extract_largest_settlement(),
            "Demonyms" : self.extract_demonyms(),
            "Population" : self.extract_population(),
            "Ethnic Groups" : self.extract_ethnic_groups(),
        }

    def extract_coordinates(self):
        DEBUG and print("@ Extracting coordinates.")
        return self.extractor.extract_pair(
            "Coordinates",
            lambda y: y.get_text().split("/")[0],
            base=self.infobox
        )

    def extract_adjacent_to(self):
        DEBUG and print("@ Extracting adjacent to.")
        return self.extractor.extract_pair(
            "Adjacent to",
            lambda y: [y.get_text() for y in y.select("li")],
            base=self.infobox
        )

    def extract_major_islands(self):
        DEBUG and print("@ Extracting major islands.")
        return self.extractor.extract_pair(
            "Major islands",
            lambda y: [y.get_text() for y in y.select("li")],
            base=self.infobox
        )

    def extract_area(self):
        DEBUG and print("@ Extracting area.")
        return self.extractor.extract_pair(
            "Area",
            lambda y: 
                self.Extractor.to_float(
                    y.get_text().split("km2")[0].replace("\xa0", "")
                ),
            base=self.infobox
        )

    def extract_area_rank(self):
        DEBUG and print("@ Extracting area rank.")
        return self.extractor.extract_pair(
            "Area rank",
            lambda y: y.get_text()[:-2],
            base=self.infobox
        )

    def extract_coastline(self):
        DEBUG and print("@ Extracting coastline.")
        return self.extractor.extract_pair(
            "Coastline",
            lambda y: 
                self.Extractor.to_float(
                    y.get_text().split("km")[0]
                ),
            base=self.infobox
        )


    def extract_highest_elevation(self):
        DEBUG and print("@ Extracting highest elevation.")
        return self.extractor.extract_pair(
            "Highest\xa0elevation",
            lambda y: 
                self.Extractor.to_float(
                    y.get_text().split("m")[0]
                ),
            base=self.infobox
        )

    def extract_highest_point(self):
        DEBUG and print("@ Extracting highest point.")
        return self.extractor.extract_pair(
            "Highest\xa0point",
            base=self.infobox
        )

    def extract_regions(self):
        DEBUG and print("@ Extracting regions.")
        def extract(y): 
            y = y.select("li")
            for i in range(len(y)): 
                items = y[i].get_text().split(" – ")
                if len(items) > 1: 
                    y[i] = items[1]
                else:
                    y[i] = y[i].get_text()
            return y

        return self.extractor.extract_pair(
            "Regions",
            select=extract,
            base=self.infobox
        )

    def extract_provinces(self):
        DEBUG and print("@ Extracting provinces.")
        def extract(y): 
            y = y.select("li")
            for i in range(len(y)): 
                items = y[i].get_text().split(" – ")
                if len(items) > 1: 
                    y[i] = items[1]
                else:
                    y[i] = y[i].get_text()
            return y

        return self.extractor.extract_pair(
            "Provinces",
            select=extract,
            base=self.infobox
        )

    def extract_largest_settlement(self):
        DEBUG and print("@ Extracting largest settlement.")
        return self.extractor.extract_pair(
            "Largest settlement",
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
            "Demonym", 
            select=extract,
            base=self.infobox
        )

    def extract_population(self):
        DEBUG and print("@ Extracting population.")

        def extractor(y):
            y = y.get_text().split(" ")[0]
            y = self.Extractor.to_int(y)
            return y 

        return self.extractor.extract_pair(
            "Population", 
            select=extractor,
            base=self.infobox
        )

    def extract_ethnic_groups(self):
        DEBUG and print("@ Extracting ethnic groups.")

        def extractor(y):
            for div in y.find_all("div", {'class' : 'hlist'}): 
                div.decompose()

            y = y.select("ul")[0].findChildren("li") 
            y = [y.get_text().strip() for y in y]
            return y

        return self.extractor.extract_pair(
            "Ethnic groups", 
            select=extractor,
            base=self.infobox
        )
