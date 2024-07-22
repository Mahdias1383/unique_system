import csv
import pandas as pd
import matplotlib.pyplot as plt
from farsi_tools import standardize_persian_text

#the list of our shopping prices of all products we want to sell.
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
    "This function creates the final data frame."
    df_combined = pd.read_csv('df_combined.csv', encoding='utf-8')
    df_combined.rename(columns={'price_product': 'others_price'}, inplace=True)
    
    #add columns. 
    df_combined["subscription"] = df_combined.duplicated(subset=["name_product"])

    #Changes cells by indexes and find subscriptions.
    df_combined.loc[10:14, 'subscription'] = True #digikala subscripted products.
    df_combined.loc[20:24, 'subscription'] = True #olfa subscripted products.

    df_combined['shopping_price'] =   list_shopping_price  #add our shopping price's column.
    df_combined['trasport_price'] =  [40000 for _ in range(25)]   #add transport price's column.
    df_combined['marketing_price'] =  [3000000 for _ in range(25)]  #add marketing price's column.
    df_combined['sales_profit'] =  [30 for _ in range(25)]  #add our profit on products column.
    df_combined['our_price'] = df_combined[['shopping_price', 'trasport_price', 'marketing_price', 'sales_profit']].sum(axis=1) #add our sell price column.
    df_combined['base_price'] = df_combined[['shopping_price', 'trasport_price', 'marketing_price']].sum(axis=1) #add the product's base prices column.
    df_combined['minimum_price'] = df_combined['others_price'] #add minimum price's column...
    for i, j in zip(range(10, 15), range(20, 25)):
        price_i = df_combined.loc[i, 'others_price']
        price_j = df_combined.loc[j, 'others_price']
        min_price = min(price_i, price_j)
        df_combined.loc[i, 'minimum_price'] = min_price
        df_combined.loc[j, 'minimum_price'] = min_price

    #add a bool column for products tha competitive range or not.
    df_combined['competitive_product'] = df_combined.apply(
        lambda row:float(row['minimum_price'] ) <= float(row['our_price']) <= float(row['base_price']), axis=1)
    
    df_combined['competitive_price-range'] = df_combined.apply(
    lambda row: f"{row['minimum_price']} – {row['base_price']}", axis=1)

    df_combined['final_profit'] = df_combined.apply(
    lambda row: float(row['our_price']) + ((float(row['sales_profit']) / 100) * float(row['our_price']) ), axis=1)

    df_combined['price_difference'] =   df_combined.apply(
        lambda row:   abs (float(row['our_price']) - float(row['others_price']))  , axis=1)
    
    df_combined.to_csv('final_data.csv', index=False) #Export the result data frame as a dataset as a csv file. 

def create_plot():
    "This function creates a plot of the columns we want from the final dataset."
    df = pd.read_csv('final_data.csv', encoding='utf-8') #reads the dataset.
    #Draw the plot for columns we want ...
    plt.figure(figsize=(10, 6)) #Plot's figure size.
    plt.plot(df['final_profit'], label='final_profit') #First column.
    plt.plot(df['final_profit'], label='our_price') #Second column.
    plt.plot(df['price_difference'], label='price_difference') #Third column.

    # Adding the titles and labels to plot.
    plt.title('Sample Plot of Columns final_profit, final_profit, and price_difference') #Plot's title.
    plt.xlabel('Index(Row_Number)') #Plot's x row's title.
    plt.ylabel('Values_in_Currency') #Plot y row's title.
    plt.legend()

    plt.savefig("output.jpg")  #Saving the figure as a jpg file.
    
    #Saving figure by changing parameter values.
    plt.savefig("output1", facecolor='y', bbox_inches="tight",
                pad_inches=0.3, transparent=True)
