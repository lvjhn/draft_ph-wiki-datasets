import pandas as pd

class Metadata: 
    def get(context, admin_level):
        basis = f"./data/{context}/metadata/basis/{admin_level}.csv"
        main  = f"./data/{context}/metadata/main/{admin_level}.csv"
        basis_df = pd.read_csv(basis)
        main_df = pd.read_csv(main)
        merged_df = pd.concat([basis_df, main_df], axis=1)

        if admin_level == "provinces":
            province_psgcs = \
                f"./data/{context}/metadata/refs/provinces.psgc.csv"
            province_psgcs_df = \
                pd.read_csv(province_psgcs) 
            merged = pd.concat([merged_df, province_psgcs_df], axis=1)

        return merged
        