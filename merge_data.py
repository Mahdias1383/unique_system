import csv
import pandas as pd
import lists

def create_data_frames(listt, file_name):
    "This function creates a data frame."
    df = pd.DataFrame(listt)
    df.to_csv(file_name, index=False)
    return df

def combine_data_frames(df1,df2,df3):
    "This function combines three data r=frames."
    df_combined = pd.concat([df1, df2, df3], ignore_index=True)
    df_combined.to_csv('df_combined.csv', index=False, encoding='utf-8')
    return df_combined
