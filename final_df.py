import csv
import pandas as pd

def create_final_dataset():
    df_combined = pd.read_csv('df_combined.csv', encoding='utf-8')

    #اضافه کردن ستون 
    df_combined["subscription"] = df_combined.duplicated(subset=["name_product"])

    # تغییر یک سلول ستون با اندیس سطر و ستون
    #digikala
    df_combined.loc[10, 'subscription'] = True
    df_combined.loc[11, 'subscription'] = True
    df_combined.loc[12, 'subscription'] = True
    df_combined.loc[13, 'subscription'] = True
    df_combined.loc[14, 'subscription'] = True
    #olfa
    df_combined.loc[20, 'subscription'] = True
    df_combined.loc[21, 'subscription'] = True
    df_combined.loc[22, 'subscription'] = True
    df_combined.loc[23, 'subscription'] = True
    df_combined.loc[24, 'subscription'] = True


    df_combined['shopping_price'] =  [1 for _ in range(25)]    
    df_combined['trasport_price'] =  [40000 for _ in range(25)]    
    df_combined['marketing_price'] =  [3000000 for _ in range(25)]    
    df_combined['sales_profit'] =  [30 for _ in range(25)]    
    df_combined['seling_price'] =  [50000 for _ in range(25)]    
    df_combined['base_price'] =  [30 for _ in range(25)]    
    df_combined['minimum_price'] =  [30 for _ in range(25)]
    df_combined['competitve_product'] =  [True for _ in range(25)]
    df_combined['final_profit'] = [30 for _ in range(25)]
    df_combined['price_difference'] = [30 for _ in range(25)]
    
    
    df_combined.to_csv('final_data.csv', index=False)
    



