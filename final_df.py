import csv
import pandas as pd
import matplotlib.pyplot as plt

list_shopping_price=[
    44860600,  
    14054400,  
    44860600,  
    2151400,   
    44860600,
    9576960,   
    59000000,  
    5783840, 
    11980000,   
    8217190,     
    2950000,  
    5295000,  
    4795000,  
    320000000,  
    7620460,
    43700000, 
    10300000,  
    25100000,  
    6240000,
    7750000,
    3160000,
    5780000,
    34500000,
    4950000,
    7750000,
    ]
def create_final_dataset():
    df_combined = pd.read_csv('df_combined.csv', encoding='utf-8')
    df_combined.rename(columns={'price_product': 'others_price'}, inplace=True)
   
    #اضافه کردن ستون 
    df_combined["subscription"] = df_combined.duplicated(subset=["name_product"])

    # تغییر یک سلول ستون با اندیس سطر و ستون
    #digikala
    df_combined.loc[10:14, 'subscription'] = True
    #olfa
    df_combined.loc[20:24, 'subscription'] = True


    df_combined['shopping_price'] =   list_shopping_price #[1 for _ in range(25)]    
    df_combined['trasport_price'] =  [40000 for _ in range(25)]    
    df_combined['marketing_price'] =  [3000000 for _ in range(25)]    
    df_combined['sales_profit'] =  [30 for _ in range(25)] 
    
    df_combined['our_price'] = df_combined[['shopping_price', 'trasport_price', 'marketing_price', 'sales_profit']].sum(axis=1)
    df_combined['base_price'] = df_combined[['shopping_price', 'trasport_price', 'marketing_price']].sum(axis=1)
    
    #minimum price
    df_combined['minimum_price'] = df_combined['others_price']
    for i, j in zip(range(10, 15), range(20, 25)):
        price_i = df_combined.loc[i, 'others_price']
        price_j = df_combined.loc[j, 'others_price']
        min_price = min(price_i, price_j)
        df_combined.loc[i, 'minimum_price'] = min_price
        df_combined.loc[j, 'minimum_price'] = min_price

    # ditect competitve_product
    df_combined['competitve_product'] = df_combined.apply(
        lambda row:float(row['minimum_price'] ) <= float(row['our_price']) <= float(row['base_price']),
    axis=1
    )

    df_combined['competitive_price-range'] = df_combined.apply(
    lambda row: f"{row['minimum_price']} – {row['base_price']}",
    axis=1
)

    df_combined['final_profit'] = df_combined.apply(
    lambda row: float(row['our_price']) + ((float(row['sales_profit']) / 100) * float(row['our_price']) ),
    axis=1)

    df_combined['price_difference'] =   df_combined.apply(
        lambda row:   abs (float(row['our_price']) - float(row['others_price']))  ,
         axis=1  )
    
    df_combined.to_csv('final_data.csv', index=False)


def create_plot():
    df = pd.read_csv('final_data.csv', encoding='utf-8')
    # Plot the columns A, B, and C
    plt.figure(figsize=(10, 6))
    plt.plot(df['final_profit'], label='final_profit')
    plt.plot(df['final_profit'], label='our_price')
    plt.plot(df['price_difference'], label='price_difference')

    # Adding titles and labels
    plt.title('Sample Plot of Columns final_profit, final_profit, and price_difference')
    plt.xlabel('Index(Row_Number)')
    plt.ylabel('Values_in_Currency')
    plt.legend()

    
    # Show the plot
    # plt.show()
    # Saving the figure.
    plt.savefig("output.jpg")
    
    # Saving figure by changing parameter values
    plt.savefig("output1", facecolor='y', bbox_inches="tight",
                pad_inches=0.3, transparent=True)




