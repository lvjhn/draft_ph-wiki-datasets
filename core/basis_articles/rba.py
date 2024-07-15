import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd 

class RegionBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Regions)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "location",
            "region", 
            "psgc", 
            "island_group", 
            "regional_center",
            "component_lgus", 
            "area",
            "population_2020",
            "density_2020" 
        ]

        table_filters = self.extractor.from_headers([
            "Location", 
            "Region", 
            "PSGC",
            "Island group",
            "Regional center",
            "Component local government units",
            "Area", 
            "Population",
            "Density"
        ])
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[1:-1]

        # create dataframe 
        df = pd.DataFrame(data, columns=headers) 

        # drop location field (empty)
        df = df.drop("location", axis=1)

        #
        # Region Data
        # 

        df["region_abbr"] = \
            df["region"].apply(
                lambda x: self.Extractor.first_or_null(r"\((.*)\)", x)
            )

        df["region"] = \
            df["region"].apply(
                lambda x: self.Extractor.first_or_null(r"(.*)\(.*\)", x)
            )

        df = df.drop("region", axis=1)
        
        #
        # Regional Center
        # 

        df["regional_center"] = \
            df["regional_center"].apply(
                lambda x: 
                    x.replace("(interim/de facto)", "").split(" and ") 
            )

        #
        # Component LGUs
        # 

        df["n_lgus"] = \
            df["component_lgus"].apply(
                lambda x: 
                    self.Extractor.to_int(x.split("\n")[0])
            )

        df["lgus"] = \
            df["component_lgus"].apply(
                lambda x: (
                    [
                        self.Extractor.normalize(
                            x, 
                            remove_brackets=True,
                            remove_parentheses=True
                        )
                        for x in x.split("\n")[1].split("|")
                    ]
                ) 
            )

        df = df.drop("component_lgus", axis=1)

        #
        # Area
        # 
        df = self.Extractor.area_split(df, "area")

        #
        # Population
        # 
        df["population_count_2020"] = \
            df["population_2020"].apply(
                lambda x: 
                    self.Extractor.to_float(x.split(" ")[0].strip())
            )

        df["population_pa_2020"] = \
            df["population_2020"].apply(
                lambda x: 
                    self.Extractor.to_float(
                        self.Extractor.first_or_null(r"\((.*)%\)", x)
                    )
            )

        df = df.drop("population_2020", axis=1)

        #
        # Density
        # 
        df = self.Extractor.density_split(df, "density_2020")

        #
        # Region Links
        #
        links = self.extractor.extract_table_links(table_filters, 1)
        df["article_link"] = links

        return df