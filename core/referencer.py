from core.metadata import Metadata

class Referencer: 
    def island_groups(
        context
    ): 
        locations = Metadata.get(context, "island-groups")
        
        locations["Ref. Id"] = [ 
            "ig:" + str(locations["Island Group"][i])
            for i in range(len(locations))
        ]

        return locations

    def regions(
        context
    ): 
        locations = Metadata.get(context, "regions")

        locations["Ref. Id"] = [ 
            "r:" + str(locations["PSGC"][i]) + "00000000"
            for i in range(len(locations))
        ]

        return locations

    def provinces(
        context
    ): 
        locations = Metadata.get(context, "provinces")
        
        locations["Ref. Id"] = [ 
            "p:" + str(locations["PSGC"][i])
            for i in range(len(locations))
        ]
        
        return locations

    def districts(
        context
    ): 
        locations = Metadata.get(context, "districts")
        
        locations["Ref. Id"] = [ 
            "d:" + str(locations["District Key"][i])
            for i in range(len(locations))
        ]

        return locations

    def municities(
        context
    ): 
        locations = Metadata.get(context, "municities")
        
        locations["Ref. Id"] = [ 
            "m:" + str(locations["PSGC"][i]).replace(".0", "")
            for i in range(len(locations))
        ]
        
        return locations

    def barangays(
        context
    ): 
        locations = Metadata.get(context, "barangays")

        locations["Ref. Id"] = [ 
            "b:" + str(locations["adm4_psgc"][i])
            for i in range(len(locations))
        ]

        return locations



