import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd

class CityBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Cities)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "coordinates",
           "city",
           "population_2020",
           "area",
           "density",
           "province", 
           "region",
           "legal_class", 
           "charter",
           "approval",
           "ratification"
        ]

        table_filters = self.extractor.from_headers(
            [
                "City",
                "Population",
                "Area",
                "Density",
                "Province",
                "Region",
                "Legal class",
                "Charter",
                "Date of"
            ],
            header_index=1
        )
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[3:-2]


        # convert to dataframe 
        df = pd.DataFrame(data, columns=headers)

        #
        # Coordinates
        #  
        df = df.drop("coordinates", axis=1)

        #
        # Population
        # 
        df["population_2020"] = \
            df["population_2020"].apply(
                lambda x: 
                    self.Extractor.to_int(
                        self.Extractor.normalize(
                            x, 
                            remove_brackets=True
                        )
                    )
            ) 
        
        #
        # Area
        # 
        df = self.Extractor.area_split(df, "area")

        #
        # Density
        # 
        df = self.Extractor.density_split(df, "density")

        #
        # Province
        # 
        df["province"] = \
            df["province"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Charter
        # 
        df["charter"] = \
            df["charter"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Approval
        # 
        df["approval"] = \
            df["approval"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )
        
        #
        # Ratification
        # 
        df["ratification"] = \
            df["ratification"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Convert to dates
        # 
        df = self.Extractor.date_split(df, "approval")
        df = self.Extractor.date_split(df, "ratification")

        return df