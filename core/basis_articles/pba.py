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
            "ISO",
            "Province", 
            "Capital", 
            "Population p.a. (2020)",
            "Population Count (2020)",
            "Area",
            "Density (2020)", 
            "Founded",
            "Island Group",
            "Region",
            "Municipalities",
            "Cities",
            "Barangays"     
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
        )[2:-2]


        # create dataframe 

        df = pd.DataFrame(data, columns=headers) 

        #
        # Province
        # 
        df["Province"] = \
            df["Province"].apply(
                lambda x: 
                    self.Extractor.normalize(x, remove_brackets=True)
            )

        #
        # Capital
        # 
        df["Capital"] = \
            df["Capital"].apply(
                lambda x: 
                    self.Extractor.normalize(x, remove_brackets=True)
                        .replace("†", "")
                        .strip()
            )

        #
        # Population 
        # 
        df["Population p.a. (2020)"] = \
            df["Population p.a. (2020)"].apply(
                lambda x: 
                    self.Extractor.deperc(x)
            )
        
        df["Population Count (2020)"] = \
            df["Population Count (2020)"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Area 
        # 
        df = self.Extractor.area_split(df, "Area")

        #
        # Density 
        # 
        df = self.Extractor.density_split(df, "Density (2020)")


        #
        # Founded 
        # 
        df["Founded"] = df["Founded"].apply(
            lambda x:   
                self.Extractor.normalize(
                    x, 
                    remove_brackets=True, 
                    trim=True
                )
        )
        df = self.Extractor.date_split(df, "Founded")

        #
        # LGUs 
        # 
        df["Municipalities"] = \
            df["Municipalities"].apply(
                lambda x: self.Extractor.to_int(x)
            ) 

        df["Cities"] = \
            df["Cities"].apply(
                lambda x: self.Extractor.to_int(x)
            )    

        df["Barangays"] = \
            df["Barangays"].apply(
                lambda x: self.Extractor.to_int(x)
            )       

        #
        # Region Links
        #
        links = self.extractor.extract_table_links(table_filters, 1)
        df["Article Link"] = links     

        return df 