from core.metadata import Metadata
import pandas as pd 

class Locator: 
    def load_reference(context, admin_level):
        filepath = f"./data/{context}/metadata/reference/{admin_level}.csv"
        df = pd.read_csv(filepath)
        return df

    def island_groups(
        context
    ): 
        locations = Locator.load_reference(context, "island-groups")
        return locations

    def regions(
        context,
        island_group=None
    ): 
        locations = Locator.load_reference(context, "regions")

        if island_group:
            locations = locations.query(f"`Island Group` == '{island_group}'")

        return locations

    def provinces(
        context,
        island_group=None,
        region_name=None,
        region_code=None
    ): 
        locations = Locator.load_reference(context, "provinces")
        
        if island_group:
            locations = locations.query(f"`Island Group` == '{island_group}'")

        elif region_name:
            locations = locations.query(f"`Region.1` == '{region_name}'")

        elif region_code:
            regions = Locator.regions(context)
            region_name = str(
                regions
                    .query(f"`Ref. Id` == 'r:{region_code}'")
                    .iloc[0]['Region']
            ).strip()
            locations = locations.query(f"`Region.1` == '{region_name}'")

        return locations

    def districts(
        context,
        island_group=None,
        region_name=None,
        region_code=None,
        province_name=None,
        province_code=None
    ): 
        locations = Locator.load_reference(context, "districts")
      
        if island_group:
            regions = Locator.regions(context)
            ig_regions = list(
                regions
                    .query(f"`Island Group` == '{island_group}'")
                    ["Region (Abbr)"]
            )
            ig_regions = [x.replace("Region ", "") for x in ig_regions]
            locations = locations[locations["Region"].isin(ig_regions)]
        
        elif region_name:
            regions = Locator.regions(context)
            region_abbr = regions.query(f"Region == '{region_name}'")
            region_abbr = list(region["Region (Abbr)"])[0].replace("Region ", "")
            locations = locations.query(f"`Region` == '{region_abbr}'")

        elif region_code:
            regions = Locator.regions(context)
            region_abbr = regions.query(f"`Ref. Id` == 'r:{region_code}'")
            region_abbr  = list(region["Region (Abbr)"])[0].replace("Region ", "")
            locations = locations.query(f"`Region` == '{region_abbr}'")

        elif province_name:
            locations = locations.query(f"`Province` == '{province_name}'")

        elif province_code:
            provinces = Locator.provinces(context)
            province_name = provinces.query(f"`Ref. Id` == 'p:{province_code}'")
            province_name = list(province_name["Province"])[0]
            locations = locations.query(f"`Province` == '{province_name}'")
        
        return locations

    def municities(
        context,
        island_group=None,
        region_name=None,
        region_code=None,
        province_name=None,
        province_code=None,
        district_slug=None, 
        district_code=None,
        district_code_slug=None
    ): 
        locations = Locator.load_reference(context, "municities")
       
        if island_group:
            regions = Locator.regions(context)
            ig_regions = list(
                regions
                    .query(f"`Island Group` == '{island_group}'")
                    ["Region"]
            )
            locations = locations[locations["Region"].isin(ig_regions)]
        
        elif region_name:
            regions = Locator.regions(context)
            region = regions.query(f"Region == '{region_name}'")
            region_name = list(region["Region"])[0]
            locations = locations.query(f"`Region` == '{region_name}'")

        elif region_code:
            regions = Locator.regions(context)
            region_abbr = regions.query(f"`Ref. Id` == 'p:{region_code}'")
            region_abbr = list(region_abbr["Region"])[0]
            locations = locations.query(f"`Region` == '{region_abbr}'")

        elif province_name:
            locations = locations.query(f"`Province` == '{province_name}'")

        elif province_code:
            provinces = Locator.provinces(context)
            province_name = provinces.query(f"`Ref. Id` == 'p:{province_code}'")
            province_name = list(province_name["Province"])[0]
            locations = locations.query(f"`Province` == '{province_name}'")
        
        elif province_code:
            provinces = Locator.provinces(context)
            province_name = provinces.query(f"`Ref. Id` == 'p:{province_code}'")
            province_name = list(province_name["Province"])[0]
            locations = locations.query(f"`Province` == '{province_name}'")
        
        elif district_slug: 
            tokens = district_slug.split("|")
            locations = locations.query(
                f"`Province` == '{tokens[0]}'"
            )
            locations = locations.query(
                f"`District` == '{tokens[1]}'"
            )           
            
        elif district_code_slug: 
            tokens = district_code_slug.split("|")
            
            province_code = tokens[0]
            provinces = Locator.provinces(context)
            province_name = provinces.query(f"`Ref. Id` == 'p:{province_code}'")
            province_name = list(province_name["Province"])[0]

            locations = locations.query(
                f"`Province` == '{province_name}'"
            )
            locations = locations.query(
                f"`District` == '{tokens[1]}'"
            )
    


        return locations

    def barangays(
        context
    ): 
        locations = Locator.load_reference(context, "barangays")

        return locations



