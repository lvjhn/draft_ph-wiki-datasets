import core.helpers as helpers
from core.basis_article import BasisArticle

class DistrictBasisArticle(BasisArticle): 
    def __init__(self, *args, **kwargs): 
        article = "Philippines (Districts)"
        BasisArticle.__init__(self, article, *args, **kwargs)

    def extract_metas(self): 
        # extract main table data
        headers = [
               
        ]
        
        data = self.extractor.extract_table_body(
            "table", 
            filter_=self.extractor.from_headers([
                
            ])
        )[:-2]

