import core.helpers as helpers

from core.article import Article

class MainArticle(Article):
    def __init__(self):
        Article.__init__(self, *args, **kwargs) 
