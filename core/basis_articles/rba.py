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
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=self.extractor.from_headers([
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
        )[:-1]

        # create dataframe 
        df = pd.DataFrame(data, columns=headers) 

        # drop location field (empty)
        df = df.drop("location", axis=1)

        #
        # Region Data
        # 

        # extract location names
        df["region_abbr"] = \
            df["region"].apply(
                lambda x: self.Extractor.first_or_null(r"\((.*)\)", x)
            )

        df["region_name"] = \
            df["region"].apply(
                lambda x: self.Extractor.first_or_null(r"(.*)\(.*\)", x)
            )

        # drop full region name 
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
                    self.Extractor.to_int(x.split("\n")[1])
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
                        for x in x.split("\n")[2].split("|")
                    ]
                ) 
            )

        df = df.drop("component_lgus", axis=1)

        #
        # Area
        # 
        df["area_km2"] = \
            df["area"].apply(
                lambda x: 
                    self.Extractor.to_float(x.split("km2")[0].strip())
            )

        df["area_mi2"] = \
            df["area"].apply(
                lambda x: 
                    self.Extractor.to_float(
                        self.Extractor.first_or_null(r"\((.*)\ssq\smi\)", x)
                    )
            )

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

        #
        # Density
        # 
        df["density_km2_2020"] = \
            df["density_2020"].apply(
                lambda x: 
                    self.Extractor.to_float(x.split("/km2")[0].strip())
            )

        df["density_mi2_2020"] = \
            df["density_2020"].apply(
                lambda x: 
                    self.Extractor.to_float(
                        self.Extractor.first_or_null(r"\((.*)/sq\smi\)", x)
                    )
            )

        return df