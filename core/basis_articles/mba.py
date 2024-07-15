import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd

class MunicityBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Municities)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "Municity", 
            "Population (2020)",
            "Area (km2)",
            "Density (2020)", 
            "Barangays", 
            "Class", 
            "Province",
        ]

        table_filters = self.extractor.from_headers([
            "City or municipality", 
            "Population", 
            "Area", 
            "PD",
            "Brgy", 
            "Class",
            "Province"
        ])
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[1:-1]

        # convert to dataframe 
        df = pd.DataFrame(data, columns=headers)

        #
        # Name 
        # 
        df["Municity"] = \
            df["Municity"].apply(
                lambda x: 
                    x.replace("*", "")
            )

        #
        # Population
        # 
        df["Population (2020)"] = \
            df["Population (2020)"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        #
        # Area
        # 
        df["Area (km2)"] = \
            df["Area (km2)"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        #
        # Population Density
        # 
        df["Density (2020)"] = \
            df["Density (2020)"].apply(
                lambda x: self.Extractor.to_float(x)
            )   

        #
        # Barangays
        # 
        df["Barangays"] = \
            df["Barangays"].apply(
                lambda x: self.Extractor.to_int(x)
            )   

        #
        # Island Group Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["Article Link"] = links[:-1]
      
        #
        # Create key
        # 
        df["Distry Key"] = [ 
            df["Province"][i] + "|" + df["Municity"][i]
            for i in range(len(df))
        ]
                  

        return df