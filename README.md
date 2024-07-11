# ph-wiki-datasets 
-------
This is aggregation and helper library/repository for Philippine-related 
datasets sourced from Wikipedia for machine learning purposes, used in a related
exploratory [research paper]() [TODO]. 

This also includes open-source/public-domain SVG maps of the Philippines at different 
administrative levels and GeoJSON data from external sources. 

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
for the project. It utilizes the `requests` library and `curl` system calls under 
the hood.

### `Scraper` 
The `Scraper` class is used to download Wikipedia articles and save them into 
specific locations.

### `Extractor` 
The `Extractor `class contains simple helper method for extracting basic information
from Wikipedia articles involved in this project. 

### `Article`
The `Article` class is mapped to an article (`.html` file) via its name and 
contains an `Extractor` (via class composition). It provides even more abstractions
to the extractor class for `Article` related queries. 

### `BasisArticle` (extends `Article`)
The `BasisArticle` is a simple extension of the `Article` class for base articles. 

It has different subclasses (for each administrative-level)

* `IslandGroupBasisArticle` - for island groups
* `RegionBasisArticle` - for regions 
* `ProvinceBasisArticle` - for provinces 
* `CitiesBasisArticles` - for cities 
* `MunicitiesBasisArticles` - for municipalities/cities (cities)

### `MainArticle` (extends `Article`)
The `MainArticle` class is used for the articles of the specific LGUs instead
of the articles that contain the tabulations as in the **"Basis"** articles.

It has different subclasses (for each administrative-level)

* `IslandGroupArticle` - for island groups
* `RegionArticle` - for regions 
* `ProvinceArticle` - for provinces 
* `CitiesArticle` - for cities 
* `MunicitiesArticle` - for municipalities/cities (cities)

