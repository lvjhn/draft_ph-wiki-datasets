import core.helpers as helpers
from core.main_article import MainArticle

class DistrictArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(article, *args, **kwargs)

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

        data = self.extractor.extract_table_body(
            "table", 
            filter_=lambda x, h, t: (
                "Group" in t and
                "Largest city" in t and 
                "Population" in t and 
                "p.a." in t and
                "Area" in t and 
                "Density" in t
            ) 
        )   

        # extract major islands 
        mi_table = self.subsection(("Islands",)) 
        
        mi_table = self.Extractor(str(mi_table)).select_filtered(
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
            items = self.extract_list("ol", base=col)[1:]
            data[i].append(items)

        # normalize data
        df = pd.DataFrame(data, columns=headers)
    
        df["population_2020"] = \
            df["population_2020"].apply(
                lambda x: self.Extractor.numberize(x)
            )

        df["population_2010"] = \
            df["population_2010"].apply(
                lambda x: self.Extractor.numberize(x)
            )

        df["pa"] = \
            df["pa"].apply(
                lambda x: self.Extractor.deperc(x)
            )
        pd.set_option('display.max_columns', None)

        df["area_km2"] = \
            df["area_km2"].apply(
                lambda x: self.Extractor.numberize(x)
            )

        df["area_mi2"] = \
            df["area_mi2"].apply(
                lambda x: self.Extractor.numberize(x)
            )

        df["density_km2"] = \
            df["density_km2"].apply(
                lambda x: self.Extractor.numberize(x)
            )

        df["density_mi2"] = \
            df["density_mi2"].apply(
                lambda x: self.Extractor.numberize(x)
            )
        
        df.to_csv()
        
