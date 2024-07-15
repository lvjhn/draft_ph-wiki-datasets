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
           "Coordinates",
           "City",
           "Population (2020)",
           "Area",
           "Density",
           "Province", 
           "Region",
           "Legal Class", 
           "Charter",
           "Approval",
           "Ratification"
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
        df = df.drop("Coordinates", axis=1)

        #
        # Population
        # 
        df["Population (2020)"] = \
            df["Population (2020)"].apply(
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
        df = self.Extractor.area_split(df, "Area")

        #
        # Density
        # 
        df = self.Extractor.density_split(df, "Density")

        #
        # Province
        # 
        df["Province"] = \
            df["Province"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Charter
        # 
        df["Chater"] = \
            df["Charter"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Approval
        # 
        df["Approval"] = \
            df["Approval"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )
        
        #
        # Ratification
        # 
        df["Ratification"] = \
            df["Ratification"].apply(
                lambda x: 
                    self.Extractor.normalize(
                        x,
                        remove_brackets=True
                    )
            )

        #
        # Convert to dates
        # 
        df = self.Extractor.date_split(df, "Approval")
        df = self.Extractor.date_split(df, "Ratification")

        #
        # District Links
        #
        links = self.extractor.extract_table_links(table_filters, 1)
        df["Article Link"] = links    

        return df