# ph-wiki-datasets 
-------
This is aggregation and helper library/repository for Philippine-related 
datasets sourced from Wikipedia for machine learning purposes, used in a related
exploratory [research paper]() [TODO]. 

This also includes open-source/public-domain SVG maps of the Philippines at different 
administrative levels and GeoJSON data from external sources. 


### Latest Collection Date
For reference, the latest collection date was made in July 12, 2024. 
Depending on several circumstances and commitments, this dataset "may" or "may not" be updated.
I may not fully attend on maintaining recency of this dataset at full time.

You may freely fork this repository, modify it, extend if you wish, and recollect info. for 
future updated versions of the involved data.

## General Statistics (Philippines)
To illustrate the complexity of the dataset. The following is an overview 
of the different counts of LGUs at each administrative level in the Philippines.
* **No. of Regions** - 17 
* **No. of Provinces** - 82 
* **No. of Districts** - 253 
* **No. of Cities** - 149  
* **No. of Municipalities** - 1,494 
* **No. of Barangays** - 42,029 

## Raw Datasets Included 
1. **`Set A` : 'Basis" Wikipedia Articles**
    - **Source**: `https://wikipedia.org`
    - Wikipedia articles of the Philippines for different administrative 
      levels are from the following:
        * **LGU Listings** 
            - **Description**
                - These articles have tables in them that enumerate and tabulate 
                component LGUs together with some general information about each
                of them. 
                - They serve as the basis (foundation) for collecting other information.
            - **Articles Included**
                - **Regions of the Philippines** 
                    - https://en.wikipedia.org/wiki/Regions_of_the_Philippines
                - **Provinces of the Philippines**
                    - https://en.wikipedia.org/wiki/Provinces_of_the_Philippines
                - **Congressional Districts of the Philippines**
                    - https://en.wikipedia.org/wiki/Congressional_districts_of_the_Philippines
                - **List of Cities in the Philippines**
                    - https://en.wikipedia.org/wiki/List_of_cities_in_the_Philippines
                - **List of Municipalities/Cities in the Philippines** 
                    - https://en.wikipedia.org/wiki/List_of_cities_and_municipalities_in_the_Philippines

1. **`Set B`: SVG Maps**
    - **Description** 
        - These are raw SVG maps of the Philippines each having borders
          on different administrative levels. 
    - **Sources**
        * **Nation-Level** - no borders (plain map)
            * **Link**: https://simplemaps.com/svg/country/ph
            * **License**: Free to Use for Commercial and Personal Use
            * **Size**: 56.6 KiB 
        * **Island-Group Level**  
            * Derived from region-level map by applying union operation on 
              regions on islands on the same island group 
              (i.e. Luzon, Visayas, and Mindanao).
        * **Region-Level** - region-level borders 
            * **Link**: https://commons.wikimedia.org/wiki/File:Blank_map_of_the_Philippines_%28Regions%29.svg
            * **License**: Creative Commons Attribution-Share Alike 4.0 International
            * **Size**: 10.5 MiB
        * **Province Level** - province-level borders
            - **Source**: https://mapsvg.com/maps/philippines
            - **License**: https://creativecommons.org/licenses/by/4.0/
            - **Size** : 97.6 KiB
        * **District Level** - district-level borders
            - Derived from municipality/city (municity) level maps by applying union operation
              on municipalities on the same district using Shapely (Python
              library for geometric operations/transformations).
            - > The term `municity` is borrowed for its use by this external repository
                https://github.com/faeldon/philippines-json-maps/tree/master/2023/
                to refer to LGUs that can either be a `municipality` or `city`.

        * **Municipality/City Level** - municipality/city-level borders
            - **Source**: https://commons.wikimedia.org/wiki/File:Municipalities_of_the_Philippines.svg
            - **License**: Public Domain
            - **Size**: 47.3 MiB
        * **Barangay Level** - barangay-level borders
            - **Not Included** - Future Recommendation

1. **`Set C` : List/Outline of Barangays (2016, 2017, and 2019)** 
    - **Source**:  https://github.com/flores-jacob/philippine-regions-provinces-cities-municipalities-barangays
    - **License**: MIT

1. **`Set D` : Level-Specific Wikipedia Articles (Corpus)** 
    - **Description** 
        - Wikipedia articles are collected at each administrative level 
            - **Island Group** - 3 articles
            - **Region** - 17 articles 
            - **Province** - 82 provinces 
            - **Municities** - 1642 municities 
    - **Sources** 
        - The name of articles to collect are identified by tables extracted 
          from the base articles in **Set A**. These tables contain information
          about the different LGUs under a certain context (e.g. region, province,
          district, municity)
        
1. **`Set E` : General Information about Locations**
    - **Description** 
        - Each island group, region, province, district, and municity collected
          in this dataset has general information collected from their respective
          articles. For example, each province's baic information such as 
          population, area, density, highest elevation, zip code, and the like 
          are collected.
    - **Sources**   
        - These information are scraped/extracted from each article involved
          in `Set D` as well as some information from the tables in `Set A`.

1. **`Set F` : Articles Divided into Sections and Subsections**
    - **Description** 
        - The articles can be divided into section and subsection. Datasets
          are not made for this, rather, a utility class is used to extract
          information from articles.
    - **Sources** 
        - These information are scraped/extracted from each articles involved 
          in `Set D`. As mentioned, no real datasets are stored, rather a
          utility class can be used on an article to extract the sections and 
          subsections.  

## API 
This project is at `experimental` and `exploratory` stage only. 
It is not intended for production. The APIs may change due to changes along
the way or due to changes in the APIs of external libraries used. Please
use at *your own risk* (at your own discretion). 

### `Client` 
The `Client` class is used to download Wikipedia articles and other necessary files
for the project. It utilizes the `requests` library.

### `Scraper` 
The `Scraper` class uses the client is used to download Wikipedia articles and 
save them into specific locations.

### `Extractor` 
The `Extractor `class contains simple helper method for extracting basic information
from Wikipedia articles involved in this project. 

### `Article`
The `Article` class is mapped to an article (`.html` file) via its name and 
contains an `Extractor` (via class composition). It provides even more abstractions
to the extractor class for `Article` related queries. Functions for basic partitioning 
of an article into subsections is provided in this class.

### `BasisArticle` (extends `Article`)
The `BasisArticle` is a simple extension of the `Article` class for base articles. 

It has different subclasses (for each administrative-level)

* `IslandGroupBasisArticle` - for island groups
* `RegionBasisArticle` - for regions 
* `ProvinceBasisArticle` - for provinces 
* `CitiesBasisArticles` - for cities 
* `MunicitiesBasisArticles` - for municipalities/cities (nunicities)

### `MainArticle` (extends `Article`)
The `MainArticle` class is used for the articles of the specific LGUs instead
of the articles that contain the tabulations as in the **"Basis"** articles.

It has different subclasses (for each administrative-level)

* `NationalArticle` - for national article
* `IslandGroupArticle` - for island groups
* `RegionArticle` - for regions 
* `ProvinceArticle` - for provinces 
* `CitiesArticle` - for cities 
* `MunicitiesArticle` - for municipalities/cities (municities)

### `Map` 
The map is a simple abstraction of map data powered by two simple yet very useful 
and powerful libraries `Shapely` to represent, transform, and operate on polygonal 
shapes in map data and `SVGWrite` for creating/visualizing the geometries made
in `Shapely`. The main goal of the map class is to abstract maps at different 
adminisrative levels and apply basic operations such as applying unions on 
components under the same over-arching LGU (e.g. district-municity) to create
derived maps as well as creating a simple adjacency matrix for each map level. 

## `Locations` 
The locations class is a static class that can be used to quickly list down
or access locations and relevant links.

```python
from ph_wiki_datasets import Locations

# Accessors (Multi-Results)
Locations.island_groups()           
[
    { "id" : 1, "island_group" : "Luzon"    , "article_uri" : "Luzon"    }, 
    { "id" : 2, "island_group" : "Visayas"  , "article_uri" : "Visayas"  }, 
    { "id" : 3, "island_group" : "Mindanao" , "article_uri" : "Mindanao" }
]

Locations.regions()  
{ 
    { 
        "ref_id"        : "[REF-ID]"
        "id"            : "[PSGC-CODE]", 
        "island_group"  : "Luzon", 
        "region_name"   : "Bicol Region" , 
        "article_uri"   : "Bicol_Region"
    },
    ...
}

Locations.provinces()
{ 
    { 
        "ref_id"        : "[REF-ID]",
        "id"            : "[PSGC-CODE]", 
        "island_group"  : "Luzon", 
        "region_name"   : "Bicol Region" ,
        "province_name" : "Camarines Sur"
        "article_uri"   : "Camarines_Sur"
    },
    ...
}

Locations.districts()
{ 
    { 
        "ref_id"        : "[REF-ID]",
        "id"            : "[PSGC-CODE]", 
        "island_group"  : "Luzon", 
        "region_name"   : "Bicol Region" ,
        "province_name" : "Camarines Sur", 
        "district_no"   : "3"
        "article_uri"   : "Camarines_Sur"
    },
    ...
}

Locations.municities()
{ 
    { 
        "ref_id"        : "[REF-ID]",
        "id"            : "[PSGC-CODE]", 
        "island_group"  : "Luzon", 
        "region_name"   : "Bicol Region" ,
        "province_name" : "Camarines Sur", 
        "district_no"   : "3"
        "city_name"     : "Naga City",
        "article_uri"   : "Naga_City"
    },
    ...
}

### With Filter
Location.regions(island_group="Luzon")
Location.regions(island_group="Visayas")
Location.regions(island_group="Mindanao")

Location.provinces(island_group="Luzon")
Location.provinces(region_name="Bicol Region")
Location.provinces(region_code="[REGION-PSGC-CODE]")

Location.districts(island_group="Luzon")
Location.districts(region_name="Bicol Region")
Location.districts(region_code="[REGION-PSGC-CODE]")
Location.districts(province_name="Camarines Sur")
Location.districts(province_code="[PROVINCE-PSGC-CODE]")

Location.municities(island_group="Luzon")
Location.municities(region_name="Bicol Region")
Location.municities(region_code="[REGION-PSGC-CODE]")
Location.municities(province_name="Camarines Sur")
Location.municities(province_code="[PROVINCE-PSGC-CODE]")
Location.municities(district_slug="Camarines_Sur|3")
Location.municities(district_code_slug="[PROVINCE-PSGC-CODE]|3")

### Single-Item Accessor 
Locator.island_group(island_group="Luzon")

Locator.region(code="[PSGC-CODE]")
Locator.region(name="Bicol Region")

Locator.province(code="[PSGC-CODE]")
Locator.province(name="Camarines Sur")

Locator.district(code_slug="[PSGC-CODE]|3")
Locator.district(slug="Camarines_Sur|3")

Locator.municity(code="[PSGC-CODE]")
Locator.municity(slug="Camarines_Sur|Calabanga")


### Info Item 
Locator.general_info(ref_id="REF-REF-ID")
"""
{
    "ref_id" : [REF-REF-ID],
    "psgc" : [CODE]
    "coordinates" : "", 
    ...
}
"""

Locator.locate(code="[CODE]") 
{
    ... location related data ...
}

Locator.locate(ref_id="[REF-ID]") 
{
    ... location related data ...
}

```

> **Future Recommendations:** 
Usage of more complicated `geojson` libraries
may be useful in the future. At this time, the research first aims and focuses on establish
a baseline on simple to derive geographical features that can be retrieved at the `SVG` (vector
graphics) level, e.g. polygons, centroids, and adjacency matrices of neighboring
polygons. 

> **Futher Explorations:** More explorations on different aspects such as paths to other locations,
road maps, traffic maps, weather maps, contour maps, etc. can be reserved for later.

* `NationalMap` - for **island-group level borders**
* `IslandGroupMap` - for **region-level borders**
* `DistrictMap` - for **district-level borders**
* `RegionMap` - for ***region-level borders**
* `ProvinceMap` - for **province-level borders**
* `MunicityMap` - for **municity-level borders**

### `DatasetGenerator` 
This is a major class in this dataset that aims to generate datasets 
from the different items in and prepare such datasets for arbitary use later
e.g. machine learning, EDA, data visualization, etc. It provides for templates
functions for extracting information either from `Article` or `Map` objects. 

## API Design 

### General Helpers
The general helpers script contains simple and quick functions for commonly
used functions such as flattening a JSON tree.

* `flatten(tree)` - flattens a JSON tree

### **`Client`** 
The client class can be instantiated using the following syntax. 
```python
from ph_wiki_datasets import Client

# for downloading files
svg_host = Client(
    base_url="http://svg-host.com/",
    prefix="t Clientwiki/",
    download_dir="svgs/",     # optional (defaults to current directory)
)

svg_host.download("/uri", "output-file.txt")

# for extracting pages
html_host = Client(
    base_url="http://en.wikipedia.org/",
    prefix="wiki/",
    download_dir="articles/"
)

# download page into .html file
html_host.download("roygbiv", "roygbiv.html")

# extract html directly
text = html_host.data("roygbiv")

```
* The following are the properties of the class.
    - `base_url` 
        - the `base_url` to be used by the downloader
    - `prefix` 
        - the prefix `URI` to prepend to passed URIs.
    - `download_outdir` 
        - download directory for the target files 
* The client class is very minimal and straightforward and only has
    the following "public" methods. Its primarily goal is abstraction.
    - `download(url, outfile=None, format="html")` 
        - download from `url` and save to `outfile` (same filename if outfile is ommited)
    - `data(url)`
        - create a `BeautifulSoup` object from the html directly
    - `fetch_with_summary(url)` 
        - fetch with selected summary statistic such as content size and download duration 
    - `set_prefix(prefix)` 
        - sets the URI prefix of the client 


### **`Scraper`** 
This is a basic scraping utility class that makes uses of the `Client` object
to collect articles from arbitrary websites such as Wikipedia. It can be passed 
a list of articles to collect. The main purpose of the scraper is for batch
download of articles and consistent presentation of the download progress. It
also shows a summary

```python
from ph_wiki_datasets import Scraper
 
client = Client(
    base_url="https://en.wikipedia.org", 
    prefix="wiki"
)

scraper = Scraper(
    client=wikipedia_client,
    download_outdir="./data/articles",
    output_filename=lambda prefix, tail: f"~{prefix}-{tail}.txt"
)

# .add() - single item
scraper.add("Red")
scraper.add("Orange") 
scraper.add("Yellow") 
scraper.add("Green") 
scraper.add("Blue") 
scraper.add("Indigo") 
scraper.add("Violet") 

# .add_multi() - multi-item (array)
scraper.add_multi(["Black", "White", "Brown"])

scraper.scrape(verbose=True)
``` 

* The following are the properties of the class.
    - `client` 
        - the `client` object to be used by the scraper
    - `outfile_filename` 
        - a function that returns the name of the output file
    - `download_outdir`
        - download directory for the target files 
* The client class is very minimal and straightforward and only has
    the following "public" methods. Its primarily goal is abstraction.
    - `.add(tail)` 
        - adds a single item to scrape 
    - `.add_multi(tails)` 
        - adds multiple items to scrape


### **`Extractor`** 
This is a basic (limited) content extractor for Wikipedia articles with
the focus on getting most relatively "obvious: information from the articles
such as the ones on the "summary tables" shown on the top-right portion of 
Wikipedia pages as well as converting tables to CSV structure and extracting
lists to JSON trees.

```python
from ph_wiki_tables import Extractor 

article = "./data/articles/some-article.html"

extractor = Extractor(
    article, 
    load = True   # load is whether `article` parameter is a filepath or not.
                  # if load is false, the `article` argument is an HTML string.
)  

# the Extractor class can be extended, but here is the general 
# functions that it is shipped with

# == TABLE INFORMATION ===

# extract row : [1, 2, 3, 4, ...]
extractor.extract_row(table_sel, row_index, each=lambda x, i: x) 

# extract column (no headers) : [1, 2, 3, 4, ...]
extractor.extract_column(table_sel, col_index, each=lambda x, i: x)   

# simple table header extraction (horizontally/vertically): [...headers...]
extractor.extract_table_headers(table_sel, direction="H", each=lambda x, i: x)     

# simple table body extraction (horizontally/vertically): [[...row 1...], ...]
extractor.extract_table_body(table_sel, direction="H", each=lambda x, i, j: x)          

# data item: "foo" => "bar" from <tr><td>foo</td><td>bar</td></tr>
extractor.extract_pair(field, each=lambda x_: x)

# extract consecutive items in some table separated by "mergedtoprows"
extractor.extract_pairs_from_partition(start_field, each=lambda x, y: (x, y))

# == LIST ===
# extract list following a simple nested format 
extractor.extract_simple_list(table_sel, each=lambda x_: x) 
"""
1. Hello
2. Hi
3. RoyGBiv

[
    "Hello",
    "Hi",
    "RoyGBiv"
]
"""

# extract list following a simple nested format 
extractor.extract_nested_list(table_sel, each=lambda x_, parent, level: x) 
"""
1. Hello
    1. Hi
    2. Foo
2. Hi
    1. BivGRoy
3. RoyGBiv
    1. Foo
    2. Bar

{
    "Hello" : {
        "Hi"  : None, 
        "Foo" : None
    }, 
    "Hi" : {
        "BivGRoy" : None
    }, 
    "RoyGBiv" : {
        "Foo" : None, 
        "Bar" : None
    }
}
"""

# === NORMALIZATION === # 
Extractor.normalize(
    "text[4]{4}1234.*(8sf0809sf)",
    remove_brackets=True         # remove bracket [.*] from citations 
    remove_parentheses=True,     # remove parentheses (.*) 
    remove_braces=True           # remove braces {} 
    remove_digits=True           # remove digits
    remove_symbols=True          # remove symbols
    trim=True                    # trim?
)

# filter: digits | letters | symbols | hyphens | dashes | apostrophes
Extractor.filter(
    "1234jksjfs.8*(--dfsdf)",   # the string to filter
    filter="digits|letters",    # precurated sets defined in Extractors.subsets
    trim                        # trim?      
)

# searches for the pattern, gets the first occurence if exists else returns null 
Extractor.first_or_null(r"Item (.*) metI", "Item (Foo) metI")  
Extractor.all_or_null(r"(.*)", "(foo)(bar)(baz)") 

```

### `Article` 
The `Article` class structures objects associated with articles and uses 
extractor objects to extract information from the article's source. It abstracts
basic and obvious information that can be extracted from Wikipedia articles. It
is a base class for different subclasses such as `BasisArticle` and `MainArticle`. 
It can used directly as well as it is used to group the `BasisArticle` and `MainArticle` 
subclasses. 

It has some utility methods for partitioning articles into sections and subsections.

```python
from ph_wiki_datasets import Article 

article = Article(
    "hello",

    # optional, downloads article automatically (default, true - uses DefaultWikipediaScraper)
    download = True     

    # the scraper uses for this article
    scraper  = DefaultWikipediaScraper(
        client = DefaultWikipediaClient(), 
        outdir ="./data/articles/uncategorized/"
    )

    # where to load the article 
    load_from = "scraper"
    # or 
    load_from = "./data/articles/uncategorized"
)

# get all headers 
article.get_headers()       # gets headers as a nested list 
                            """
                                {
                                    "Heading 1 : sfsdfsldf" : {
                                        "Heading 2 : sdfsf", 
                                        ...
                                    }, 
                                    "Heading 1 : sfdsf " : {
                                        ...
                                    }
                                }   
                            """

# get headers by level 
article.get_headers(1)      # ["Heading 1 : A", "Heading 1 : B",  "Heading 1 : C"]
article.get_headers(2)      # ...
article.get_headers(3)      # ...
article.get_headers(4)      # ...
article.get_headers(5)      # ...
article.get_headers(6)      # ...

# get articles splitted into sections
article.top_level_sections()
""" 
{
    "Header 1" : "... text ...", 
    "Header 2" : "... text ...",
    "Header 3" : "... text ..."
}
"""

article.tree()
"""
{
    "Header 1 : Title" : {
        "_intro_" : "",
        "_outro_" : "", 
        "children" : {
            "Header 2 : Title" : {
                "_intro_" : "",
                "_outro_" : "",
                "children" : {

                }
            }
        }
    }, 
    ...
}
"""   

# aggregate content from h3 and deeper as a single text
article.aggregate(article.tree, 3)  
```

### `BasisArticle`
"Basis" articles are used in this project as a "catalog", "reference" or "index" of a 
higher-level LGU or adminisrative level to lower-level administrative level.
A basis article for "province" has a table that lists down information for lower-level
LGUs such as "cities" or "municipalities". 

1. `IslandGroupBasisArticle`
    - `extract_island_group_metas()`
        - `island_group_name` (name and code)
        - `population_2020`
        - `population_2015`
        - `area`
        - `density`
        - `regional_center`

1. `RegionBasisArticle`
    - `extract_region_metas()`
        - `region_name`
        - `psgc`
        - `island_group`
        - `regional_center`
        - `lgus`
        - `area`
        - `population`
        - `density`
        
1. `ProvinceBasisArticle`
    - `extract_province_metas()`
        - `iso`
        - `province_name`
        - `capital`
        - `population`
        - `area`
        - `density`
        - `founded`
        - `island_group`
        - `region`
        - `municipalities`
        - `cities`
        - `barangays`
    
1. `DistrictBasisArticle`
    - `extract_district_metas()`
        - `district_name`
        - `region`
        - `electorate`
        - `population`
        - `area`
        - `representative`
        - `party`

1. `CityBasisArticle`
    - `extract_city_metas()`
        - `city_name`
        - `population_2020`
        - `area`
        - `density_2020`
        - `province`
        - `region`
        - `legal_class`
        - `charter`
        - `approval`
        - `ratification`

1. `MunicityBasisArticle`
    - `extract_municities_meta()`
        - `municity_name`
        - `population_2020`
        - `area_km2`
        - `population_density_2020`
        - `barangays`
        - `class`
        - `province`

### `MainArticle`
Main article are the main source of the text related dimensions of the feature
space.

1. `IslandGroupArticle`
    - `extract_all()`
    - `extract_coordinates()`
    - `extract_adjacent_to()`
    - `extract_major_islands()`
    - `extract_area()`
    - `extract_area_rank()`
    - `extract_coastline()`
    - `extract_highest_elevation()`
    - `extract_highest_point()`
    - `extract_regions()`
    - `extract_provinces()`
    - `extract_largest_settlement()`
    - `extract_demonyms()`
    - `extract_population()`
    - `extract_ethnic_grouos()`