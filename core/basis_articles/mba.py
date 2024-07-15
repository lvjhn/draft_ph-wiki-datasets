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
            "municity", 
            "population_2020",
            "area_km2",
            "density_2020", 
            "barangays", 
            "class", 
            "province",
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
        df["municity"] = \
            df["municity"].apply(
                lambda x: 
                    x.replace("*", "")
            )

        #
        # Population
        # 
        df["population_2020"] = \
            df["population_2020"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        #
        # Area
        # 
        df["area_km2"] = \
            df["area_km2"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        #
        # Population Density
        # 
        df["density_2020"] = \
            df["density_2020"].apply(
                lambda x: self.Extractor.to_float(x)
            )   

        #
        # Barangays
        # 
        df["barangays"] = \
            df["barangays"].apply(
                lambda x: self.Extractor.to_int(x)
            )   

        #
        # Island Group Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["article_link"] = links[:-1]
      
        #
        # Create key
        # 
        df["district_key"] = [ 
            df["province"][i] + "|" + df["municity"][i]
            for i in range(len(df))
        ]
                  

        return df