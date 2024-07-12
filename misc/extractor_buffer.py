from core.extractor import Extractor

article = "./misc/data/Naga.html"
content = open(article, "r").read()

extractor = Extractor(content)

row = extractor.extract_simple_list(
    "#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(195)",
    filter_=None
)

print(row)