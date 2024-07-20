import csv
import pandas as pd

df_amazon = pd.read_csv('df_list_amazon.csv', encoding='utf-8')
df_digikala = pd.read_csv('df_digikala.csv', encoding='utf-8')
df_olfa = pd.read_csv('df_list_olfa.csv', encoding='utf-8')


df_combined = pd.concat([df_amazon, df_digikala, df_olfa], ignore_index=True)
df_combined.to_csv('df_combined.csv', index=False, encoding='utf-8')
df_combined = pd.read_csv('df_combined.csv', encoding='utf-8')

print(df_combined)



