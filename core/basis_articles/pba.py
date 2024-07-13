import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd

import datetime 

class ProvinceBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Provinces)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "iso",
            "province", 
            "capital", 
            "population_pa_2020",
            "population_count_2020",
            "area",
            "density_2020", 
            "founded",
            "island_group",
            "region",
            "municipalities",
            "cities",
            "barangays"     
        ]

        table_filters = self.extractor.from_headers([
            "ISO", 
            "Province", 
            "Capital",
            "Population",
            "Density",
            "Island group",
            "Region", 
            "Total"
        ])
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[:-2]


        # create dataframe 
        df = pd.DataFrame(data, columns=headers) 

        #
        # Province
        # 
        df["province"] = \
            df["province"].apply(
                lambda x: 
                    self.Extractor.normalize(x, remove_brackets=True)
            )

        #
        # Capital
        # 
        df["capital"] = \
            df["capital"].apply(
                lambda x: 
                    self.Extractor.normalize(x, remove_brackets=True)
                        .replace("†", "")
                        .strip()
            )

        #
        # Population 
        # 
        df["population_pa_2020"] = \
            df["population_pa_2020"].apply(
                lambda x: 
                    self.Extractor.deperc(x)
            )
        
        df["population_count_2020"] = \
            df["population_count_2020"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Area 
        # 
        df = self.Extractor.area_split(df, "area")

        #
        # Density 
        # 
        df = self.Extractor.density_split(df, "density_2020")


        #
        # Founded 
        # 
        df["founded"] = df["founded"].apply(
            lambda x:   
                self.Extractor.normalize(
                    x, 
                    remove_brackets=True, 
                    trim=True
                )
        )
        df = self.Extractor.date_split(df, "founded")

        #
        # LGUs 
        # 
        df["municipalities"] = \
            df["municipalities"].apply(
                lambda x: self.Extractor.to_int(x)
            ) 

        df["cities"] = \
            df["cities"].apply(
                lambda x: self.Extractor.to_int(x)
            )    

        df["barangays"] = \
            df["barangays"].apply(
                lambda x: self.Extractor.to_int(x)
            )       

        #
        # Region Links
        #
        links = self.extractor.extract_table_links(table_filters, 1)
        df["province_links"] = links     

        return df 