import core.helpers as helpers
from core.basis_article import BasisArticle

import pandas as pd

class IslandGroupBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Island Groups)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
            "Island Group", 
            "Largest City", 
            "Population (2020)", 
            "Population (2010)", 
            "P.A.", 
            "Area (km2)",
            "Area (mi2)", 
            "Density (km2)",
            "Density (mi2)",
            "Major Islands"
        ]

        table_filters = self.extractor.from_headers([
            "Group", 
            "Largest city", 
            "Population", 
            "p.a.",
            "Area",
            "Density"
        ]) 

        data = self.extractor.extract_table_body(
            "table", 
            filter_=table_filters
        )[2:-1]

        # extract major islands 
        mi_section = self.subsection(("Islands",)) 
        
        mi_table = self.Extractor(str(mi_section)).select_filtered(
            "table", 
            lambda x, h, t: (
                "Luzon" in t and 
                "Visayas" in t and 
                "Mindanao" in t
            )
        )

        rows = mi_table.select("tbody > tr", recursive=False)
        third_row = rows[2]
        cols = third_row.select("td", recursive=False)

        for i in range(len(cols)): 
            col = cols[i]
            items = self.extractor.extract_list("ol", base=col)[1:]
            data[i].append(items)

        # normalize data
        df = pd.DataFrame(data, columns=headers)
    
        df["Population (2020)"] = \
            df["Population (2020)"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        df["Population (2020)"] = \
            df["Population (2010)"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        df["P.A."] = \
            df["P.A."].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["Area (km2)"] = \
            df["Area (km2)"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["Area (mi2)"] = \
            df["Area (mi2)"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["Density (km2)"] = \
            df["Density (km2)"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["Density (mi2)"] = \
            df["Density (mi2)"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        #
        # Island Group Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["Article Link"] = links  
    
        return df