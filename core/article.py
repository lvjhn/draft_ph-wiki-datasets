import re 

import core.helpers as helpers

from core.basis_article import BasisArticle
from core.extractor import Extractor

from bs4 import BeautifulSoup

class Article:
    def __init__(self, article, **kwargs):
        # dependency injection 
        self.Extractor = kwargs.get("Extractor", Extractor)

        # extract arguments 
        self.article = article 
        self.folder = kwargs.get("folder", "./data/articles/")
        
        # load article content
        self.content = self.load_content()

        # load extractor 
        self.extractor = self.load_extractor()

    def load_content(self):
        article_path = self.folder + "/" + self.article + ".html"
        article_path = re.sub("/+", "/", article_path)
        content = open(article_path, "r").read() 
        return content

    def load_extractor(self): 
        return self.Extractor(self.content)

    def get_headers(self, level): 
        headers = self.extractor._.select(f"h{level}")
        headers = [
            header.get_text() 
            for header in headers
        ] 
        headers = [
            self.Extractor.normalize(h, remove_brackets=True) 
            for h in headers
        ]
        return headers

    def introduction(self): 
        return self.extractor._.select("#mw-content-text")[0]

    def top_level_sections(self): 
        current = self.extractor._.select("#content h2")[0]
        
        contents = {}
        current_section = ""

        while current != None:
            # set-up header
            if current.name == "h2": 
                normal_name = \
                    self.Extractor.normalize(
                        current.get_text(), 
                        remove_brackets=True
                    )
                contents[normal_name] = ""
                current_section = normal_name

            # append content 
            contents[normal_name] += str(current)
            
            # get next sibling
            current = current.findNextSibling()

            # combine contents 
            if current is None or current.name == "h2": 
                html = ( 
                    "<div class='section'>" +
                    str(contents[current_section]) +
                    "</div>"
                )
                contents[current_section] = \
                    BeautifulSoup(html, "html.parser")

        return contents

    def content_tree(self): 
        root = self.extractor._.select(".vector-toc-contents")[0]

        tree = {}

        def visit_list(base, ul): 
            items = ul.findChildren("li")
            for item in items: 
                # extract label
                label = item.select("a > div > span")
                if len(label) < 2: 
                    continue
                label = label[1].get_text() 
                base[label] = {}

                # visit subtree
                sublist = item.select("ul")
                if len(sublist) == 0:
                    continue
                visit_list(base[label], sublist[0])

        visit_list(tree, root)
        
        return tree
        
