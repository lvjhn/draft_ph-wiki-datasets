import core.helpers as helpers

from core.article import Article

class MainArticle(Article):
    def __init__(self, article, *args, **kwargs):
        Article.__init__(self, article, *args, **kwargs) 
