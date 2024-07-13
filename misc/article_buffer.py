from core.article import Article 

article = Article("Naga", folder="./misc/data/")

print(article.subsection(("History", "Precolonial era")).get_text())