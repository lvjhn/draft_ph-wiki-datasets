from core.extractor import Extractor

article = "./misc/data/Naga.html"
content = open(article, "r").read()

extractor = Extractor(content)

row = extractor.extract_table_body(
    "table",
    filter_=lambda table, html, text: (
        "Barangay" in html and
        "Class" in html
    )
)

print(row)