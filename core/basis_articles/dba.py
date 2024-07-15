import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd
import re

class DistrictBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Districts)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "District", 
            "Region",
            "Electorate (2019)",
            "Population (2020)", 
            "Area (km2)", 
            "Representative", 
            "",
            "Party"
        ]

        table_filters = self.extractor.from_headers([
            "District", 
            "Region", 
            "Electorate", 
            "Population",
            "Area", 
            "Representative",
            "Party"
        ])
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[1:]

        # convert to dataframe 
        df = pd.DataFrame(data, columns=headers) 

        #
        # Extract district province and no. 
        #          
        def get_province_name(x):
            x = " ".join(x.split(" ")[0:-1])
            x = re.sub(r"'s$", "", x) 
            x = re.sub(r"'$", "", x) 
            return x 

        def get_district_no(x):
            x = x.split(" ")[-1]
            if x == "at-large": 
                return x
            x = self.Extractor.to_int(x)
            return x 

        df["Province"] = \
            df["District"].apply(get_province_name)

        df["District No."] = \
            df["District"].apply(get_district_no)

        df = df.drop("District", axis=1) 

        #
        # Electorate 
        # 
        df["Electorate (2019)"] = \
            df["Electorate (2019)"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Population
        # 
        df["Population (2020)"] = \
            df["Population (2020)"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Area
        # 
        df["Area (km2)"] = \
            df["Area (km2)"].apply(
                lambda x: 
                    self.Extractor.to_float(x)
            )

        #
        # District Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["Article Link"] = links

        
        #
        # Create key
        # 
        df["District Key"] = [ 
            df["Province"][i] + "|" + str(df["District No."][i])
            for i in range(len(df))
        ]
                  

        return df 
