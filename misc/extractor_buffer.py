from core.extractor import Extractor

article = "./misc/data/Naga.html"
content = open(article, "r").read()

extractor = Extractor(content)

row = extractor.extract_table_headers(
    "table",
    filter_=lambda table, html, text: (
        "Barangay" in html and
        "Class" in html
    ),
    normalize=True
)
