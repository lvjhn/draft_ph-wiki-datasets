import core.helpers as helpers
from core.basis_article import BasisArticle

class DistrictBasisArticle(BasisArticle): 
    def __init__(self, article, *args, **kwargs): 
        BasisArticle.__init__(self, *args, **kwargs)