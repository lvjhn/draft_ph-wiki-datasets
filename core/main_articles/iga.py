import core.helpers as helpers
from core.main_article import MainArticle

DEBUG = helpers.DEBUG

class IslandGroupArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(self, article, *args, **kwargs)
        self.infobox = self.extractor._.select(".infobox")[0]

    def extract_all(self):
        return {
            "coordinats" : self.extract_coordinates(),
            "adjacent_to" : self.extract_adjacent_to(),
            "major_islands" : self.extract_major_islands(),
            "area" : self.extract_area(),
            "rank" : self.extract_area_rank(),
            "coastline" : self.extract_coastline(),
            "highest_elevation" : self.extract_highest_elevation(),
            "highest_point" : self.extract_highest_point(),
            "regions" : self.extract_regions(),
            "provinces" : self.extract_provinces(),
            "largest_settlement" : self.extract_largest_settlement(),
            "demonyms" : self.extract_demonyms(),
            "population" : self.extract_population(),
            "ethnic_groups" : self.extract_ethnic_groups(),
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
            select=extract
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
            select=extract
        )

    def extract_largest_settlement(self):
        DEBUG and print("@ Extracting largest settlement.")
        return self.extractor.extract_pair(
            "Largest settlement"
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
            select=extractor
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
            select=extractor
        )
