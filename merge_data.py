import csv
import pandas as pd
import lists

# def create_data_frames(listt, file_name):

#     df = pd.DataFrame(listt, columns=["name_product", "price_product"])
#     df.to_csv(file_name, index=False)
#     return df

#     # df_amazon = pd.read_csv('df_list_amazon.csv', encoding='utf-8')
#     # df_digikala = pd.read_csv('df_digikala.csv', encoding='utf-8')
#     # df_olfa = pd.read_csv('df_list_olfa.csv', encoding='utf-8')

def create_data_frames(listt, file_name):
    df = pd.DataFrame(listt)
    df.to_csv(file_name, index=False)
    return df



def combine_data_frames(df1,df2,df3):
    df_combined = pd.concat([df1, df2, df3], ignore_index=True)
    df_combined.to_csv('df_combined.csv', index=False, encoding='utf-8')
    return df_combined



