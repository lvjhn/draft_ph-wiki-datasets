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
            "island_group", 
            "largest_city", 
            "population_2020", 
            "population_2010", 
            "pa", 
            "area_km2",
            "area_mi2", 
            "density_km2",
            "density_mi2",
            "major_islands"
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
    
        df["population_2020"] = \
            df["population_2020"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        df["population_2010"] = \
            df["population_2010"].apply(
                lambda x: self.Extractor.to_int(x)
            )

        df["pa"] = \
            df["pa"].apply(
                lambda x: self.Extractor.to_float(x)
            )
        pd.set_option('display.max_columns', None)

        df["area_km2"] = \
            df["area_km2"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["area_mi2"] = \
            df["area_mi2"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["density_km2"] = \
            df["density_km2"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        df["density_mi2"] = \
            df["density_mi2"].apply(
                lambda x: self.Extractor.to_float(x)
            )

        #
        # Island Group Links
        #
        links = self.extractor.extract_table_links(table_filters, 0)
        df["island_group_links"] = links  
    
        return df