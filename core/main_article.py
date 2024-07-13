import core.helpers as helpers

from core.article import Article

class MainArticle(Article):
    def __init__(self, article, *args, **kwargs):
        Article.__init__(self, article, *args, **kwargs) 

    def extract_all(self):
        methods = dir(self) 
        fields = {}
        for method in methods: 
            if method != "extract_all" and method.startswith("extract_"): 
                fields[method.split("extract_")[1]] = getattr(self, method)()
        return fields