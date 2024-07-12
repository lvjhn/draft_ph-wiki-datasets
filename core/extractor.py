import core.helpers as helpers
from bs4 import BeautifulSoup
import re 


class Extractor:

    DIGITS      = set("0123456789")
    LETTERS     = set("abcdefghijklmnopqrstuvwxyz")
    SYMBOLS     = set("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    HYPHEN      = set("-")
    DASH        = set("-")
    APOSTROPHE  = set("'")
    PERIOD      = set(".")


    FILTERS = {
        "digits" : DIGITS,
        "letters" : LETTERS, 
        "symbols" : SYMBOLS, 
        "hyphens" : HYPHEN,
        "dashes" : DASH, 
        "apostrophe" : APOSTROPHE, 
        "period" : PERIOD
    }

    def __init__(self, content, *args, **kwargs):
        # extract arguments 
        self.content = content 
        self._       = BeautifulSoup(self.content, "html.parser")

    def normalize(text, **kwargs): 
        if kwargs.get("remove_brackets", True):
            text = re.sub(r"\[.*\]", "", text)
        if kwargs.get("remove_parentheses", True):
            text = re.sub(r"\(.*\)", "", text)
        if kwargs.get("remove_braces", True):
            text = re.sub(r"\{.*\}", "", text)
        if kwargs.get("remove_digits", True):
            text = re.sub(r"[0-9]", "", text)
        if kwargs.get("remove_symbols", True):
            text = re.sub(
                r"\!\"\#\$\%\&\'\(\)\*\+\,\-" +
                r"\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~\"\, \"", 
                "",
                text
            )

        if kwargs.get("title_case", False):
            text = " ".join([x[0].upper() + x[1:] for x in text.split(" ")])
        
        if kwargs.get("kebab_case", False):
            text = "-".join([x[0].upper() + x[1:] for x in text.split(" ")])
        
        if kwargs.get("pascal_case", False):
            text = "".join([x[0].upper() + x[1:] for x in text.split(" ")])

        if kwargs.get("camel_case", False):
            text = "".join([x[0].upper() + x[1:] for x in text.split(" ")])
            text = text[0].lower() + text[1:]

        if kwargs.get("snake_case", True):
            text = "_".join([x for x in text.split(" ")])

        if kwargs.get("lower_case", False):
            text = text.lower()

        if kwargs.get("upper_case", False):
            text = text.upper()


        return text

    def filter(text, filter_="", trim=False, **kwargs): 
        # remove leading and trailing whitespace
        if trim: 
            text = text.strip()

        text = [x for x in text if x in filter_]    

        return text

    def first_or_null(self, pattern, text):
        res = re.findall(pattern, text).group(1)
        if len(res) < 1: 
            return None 
        return res[1]

    def all_or_null(self, pattern, text):
        res = re.findall(pattern, text) 
        if len(res) < 1: 
            return None 
        return res

    def select_filtered(self, sel, filter_):
        el = None
        if filter_ == None:
            el = self._.select(sel) 
        else: 
            el = self._.select(sel)
            el = [x for x in el if filter_(x, str(x), x.get_text())]
            if len(el) > 1 or len(el) == 0:
                raise Exception("Exactly one element must match.")
            el = el[0]
        return el

    def extract_row(
        self, 
        sel, 
        row_index, 
        filter_=None, 
        each=lambda x, i: x.get_text().strip()
    ): 
        table  = self.select_filtered(sel, filter_) 
        rows   = table.select("tbody > tr")
        row    = rows[row_index] 
        fields = row.select("td")
        res    = [each(fields[i], i) for i in range(len(fields))] 
        return res

    def extract_column(
        self, 
        sel, 
        row_index, 
        filter_=None, 
        each=lambda x, i: x.get_text().strip()
    ): 
        table  = self.select_filtered(sel, filter_) 
        fields = table.select(f"tbody > tr > td:nth-child({row_index})")
        res    = [each(fields[i], i) for i in range(len(fields))] 
        return res

    def extract_table_headers(
        self, 
        sel, 
        filter_=None, 
        each=lambda x, i: x.get_text().strip(),
        normalize=False
    ): 
        table  = self.select_filtered(sel, filter_) 
        hrow   = table.select("thead > tr")[0]
        fields = hrow.select("th")
        res    = [each(fields[i], i) for i in range(len(fields))] 

        if normalize:
            res    = [
                Extractor.normalize(x, lower_case=True, snake_case=True) 
                for x in res
            ]

        return res