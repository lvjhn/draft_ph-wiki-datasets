from unittest.mock import Mock 
from core.extractor import Extractor 
import os
import pandas as pd

from .base_test import BaseTest

class TestExtractor(BaseTest): 
    def create_extractor(self): 
        article = "./tests/data/Naga.html" 
        content = open(article, "r")
        extractor = Extractor(content) 
        return extractor
    
    def test_normalize(self): 
        text = Extractor.normalize("L[ABC]R", remove_brackets=True)
        assert text == "LR"

        text = Extractor.normalize("L(ABC)R", remove_parentheses=True)
        assert text == "LR"

        text = Extractor.normalize("L{ABC}R", remove_braces=True)
        assert text == "LR"

        text = Extractor.normalize("L012R", remove_digits=True)
        assert text == "LR"

        text = Extractor.normalize("L!!@@##R", remove_symbols=True)
        assert text == "LR"

        text = Extractor.normalize("foo bar baz", title_case=True)
        assert text == "Foo Bar Baz"
        
        text = Extractor.normalize("foo bar baz", kebab_case=True)
        assert text == "foo-bar-baz"

        text = Extractor.normalize("foo bar baz", pascal_case=True)
        assert text == "FooBarBaz"

        text = Extractor.normalize("foo bar baz", camel_case=True)
        assert text == "fooBarBaz"

        text = Extractor.normalize("foo bar baz", snake_case=True)
        assert text == "foo_bar_baz"

        text = Extractor.normalize("FOO BAR BAZ", lower_case=True)
        assert text == "foo bar baz"
        
        text = Extractor.normalize("foo bar baz", upper_case=True)
        assert text == "FOO BAR BAZ"

        text = Extractor.normalize("  TEXT  ", trim=True)
        assert text == "TEXT"

    def test_filter(self): 
        text = Extractor.filter("a1ab2bc3c", filter_=set("abc")) 
        assert text == "aabbcc"

        text = Extractor.filter("1a12a23c3", filter_=set("123")) 
        assert text == "112233"

    def test_first_or_null(self): 
        assert Extractor.first_or_null(r"\(([^(]*)\)", "[ab][cd][ef]") == None
        assert Extractor.first_or_null(r"\(([^(]*)\)", "(ab)(cd)(ef)") == "ab"

    def test_all_or_null(self): 
        assert Extractor.all_or_null(r"\(([^(]*)\)", "[ab][cd][ef]") == None
        assert (
            tuple(Extractor.all_or_null(r"\(([^(]*)\)", "(ab)(cd)(ef)")) 
            == 
            ("ab", "cd", "ef")
        )

    def test_select_filter_no_filter(self): 
        extractor = self.create_extractor()
        assert extractor.select_filtered("table").name == "table"
        
    def test_select_filter_with_filter(self): 
        extractor = self.create_extractor()

        assert extractor.select_filtered(
            "table", 
            filter_=lambda x, h, t: "Barangay" in t 
        ).name == "table"
        
        assert extractor.select_filtered(
            "table", 
            filter_=lambda x, h, t: "[INEXISTENT]" in t 
        ) is None

    def test_extract_row(self): 
        extractor = self.create_extractor()

        row = extractor.extract_row(
            "table",
            0,
            filter_=lambda x, h, t: (
                "Barangays" in t and 
                "Class" in t and
                "Population" in t and
                "Barangay head" in t
            )
        )

        assert type(row) is list 
        assert len(row) == 4
        assert row[0] == "Abella"
        
    def test_extract_column(self): 
        extractor = self.create_extractor()

        column = extractor.extract_column(
            "table",
            1,
            filter_=lambda x, h, t: (
                "Barangays" in t and 
                "Class" in t and
                "Population" in t and
                "Barangay head" in t
            )
        )

        assert type(column) is list
        assert len(column) == 27
        assert column[0] == "Urban"

    def test_extract_table_headers(self): 
        extractor = self.create_extractor()

        headers = extractor.extract_table_headers(
            "table",
            filter_=lambda x, h, t: (
                "Barangays" in t and 
                "Class" in t and
                "Population" in t and
                "Barangay head" in t
            )
        )

        assert type(headers) is list
        assert len(headers) == 4
        assert headers[0] == "Barangays"

    def test_extract_pair(self): 
        extractor = self.create_extractor()

        value = extractor.extract_pair(
            "Country", 
            select=lambda x: x.get_text().strip() + " [BAR]"
        )

        assert type(value) is str
        assert value == "Philippines [BAR]"
        
    def test_extract_pairs_from_partition(self): 
        extractor = self.create_extractor()

        pairs = extractor.extract_pairs_from_partition(
            "Area", 
            select=lambda x, y, i: x.get_text().strip() + " [BAR]"
        )

        assert type(pairs) is list 
        assert len(pairs) == 3 
        assert "Independent component city" in pairs[0]

    def test_extract_list(self): 
        extractor = self.create_extractor()

        list_ = extractor.extract_list(
            "#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(195)",
            filter_=None
        )

        assert type(list_) is list 
        assert len(list_) == 12 
        assert list_[0] == "Bacolod, Negros Occidental" 

    def test_area_split(self): 
        df = pd.DataFrame({
            "area" : [
                "1 km2 (20 sq mi)",
                "5 km2 (30 sq mi)",
                "10 km2 (40 sq mi)",
            ]
        })

        df = Extractor.area_split(df, "area")

        assert tuple(df["area_km2"]) == (1, 5, 10)
        assert tuple(df["area_mi2"]) == (20, 30, 40)

    def test_density_split(self): 
        df = pd.DataFrame({
            "density_2020" : [
                "1/km2 (20 sq mi)",
                "5/km2 (30 sq mi)",
                "10/km2 (40 sq mi)",
            ]
        })

        df = Extractor.density_split(df, "density_2020")

        assert tuple(df["density_2020_km2"]) == (1, 5, 10)
        assert tuple(df["density_2020_mi2"]) == (20, 30, 40)

    def test_date_split_item(self): 
        assert Extractor.date_split_item("2024") == (None, None, "2024")
        assert Extractor.date_split_item("4 Apr 2024") == ("4", "Apr", "2024")

    def test_date_split(self): 
        df = pd.DataFrame({
            "birthdate" : [
                "2024",
                "4 Apr 2024"
            ]
        })

        df = Extractor.date_split(df, "birthdate")

        assert "birthdate_date" in df 
        assert "birthdate_month" in df 
        assert "birthdate_year" in df 
        assert "birthdate_day" in df 

        assert tuple(df["birthdate_month"]) == (None, "Apr")
        assert tuple(df["birthdate_day"]) == (None, "4")
        assert tuple(df["birthdate_year"]) == ("2024", "2024")


    def test_extract_table_links(self): 
        content = \
            open(
                "./tests/data/basis-articles/"
                "Philippines (Island Groups).html"
            ).read()

        extractor = Extractor(content)

        links = \
            extractor.extract_table_links(
                extractor.from_headers([
                    "Group",
                    "Largest city",
                    "Population",
                    "p.a.",
                    "Area",
                    "Density"
                ]),
                0
            )
        
        assert len(links) == 3

        