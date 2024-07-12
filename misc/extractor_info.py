from core.extractor import Extractor

article = "./misc/data/Article.html"
content = open(article, "r").read()

extractor = Extractor(content)

print(extractor.info())