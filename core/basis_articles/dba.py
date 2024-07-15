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
            "district", 
            "region",
            "electorate_2019",
            "population_2020", 
            "area_km2", 
            "representative", 
            "",
            "party"
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

        df["province"] = \
            df["district"].apply(get_province_name)

        df["district_no"] = \
            df["district"].apply(get_district_no)

        df = df.drop("district", axis=1) 

        #
        # Electorate 
        # 
        df["electorate_2019"] = \
            df["electorate_2019"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Population
        # 
        df["population_2020"] = \
            df["population_2020"].apply(
                lambda x: 
                    self.Extractor.to_int(x)
            )

        #
        # Area
        # 
        df["area_km2"] = \
            df["area_km2"].apply(
                lambda x: 
                    self.Extractor.to_float(x)
            )

        #
        # District Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["article_link"] = links

        
        #
        # Create key
        # 
        df["district_key"] = [ 
            df["province"][i] + "|" + str(df["district_no"][i])
            for i in range(len(df))
        ]
                  

        return df 
