import helpers 
from core.main_article import MainArticle

class IslandGroupArticle(MainArticle): 
    def __init__(self, article, *args, **kwargs): 
        MainArticle.__init__(article, *args, **kwargs)