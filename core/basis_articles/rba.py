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
            "Location",
            "Region", 
            "PSGC", 
            "Island Group", 
            "Regional Center",
            "Component LGUs", 
            "Area",
            "Population (2020)",
            "Density (2020)" 
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
        df = df.drop("Location", axis=1)

        #
        # Region Data
        # 

        df["Region (Abbr)"] = \
            df["Region"].apply(
                lambda x: self.Extractor.first_or_null(r"\((.*)\)", x)
            )

        df["Region"] = \
            df["Region"].apply(
                lambda x: self.Extractor.first_or_null(r"(.*)\(.*\)", x)
            )

        #
        # Regional Center
        # 

        df["Regional Center"] = \
            df["Regional Center"].apply(
                lambda x: 
                    x.replace("(interim/de facto)", "").split(" and ") 
            )

        #
        # Component LGUs
        # 

        df["No. of LGUs"] = \
            df["Component LGUs"].apply(
                lambda x: 
                    self.Extractor.to_int(x.split("\n")[0])
            )

        df["LGUs"] = \
            df["Component LGUs"].apply(
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

        df = df.drop("Component LGUs", axis=1)

        #
        # Area
        # 
        df = self.Extractor.area_split(df, "Area")

        #
        # Population
        # 
        df["Population Count (2020)"] = \
            df["Population (2020)"].apply(
                lambda x: 
                    self.Extractor.to_float(x.split(" ")[0].strip())
            )

        df["Population p.a. (2020)"] = \
            df["Population (2020)"].apply(
                lambda x: 
                    self.Extractor.to_float(
                        self.Extractor.first_or_null(r"\((.*)%\)", x)
                    )
            )

        df = df.drop("Population (2020)", axis=1)

        #
        # Density
        # 
        df = self.Extractor.density_split(df, "Density (2020)")

        #
        # Region Links
        #
        links = self.extractor.extract_table_links(table_filters, 1)
        df["Article Link"] = links

        return df