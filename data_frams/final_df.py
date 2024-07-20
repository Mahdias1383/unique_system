import csv
import pandas as pd

df_combined = pd.read_csv('df_combined.csv', encoding='utf-8')

#اضافه کردن ستون 
df_combined["subscription"] = df_combined.duplicated(subset=["name_product"])

#print(df_combined)

#تغییر سلول یک ستون براساس پیداکردن مقدار یک سلول از ستون همان سطر
df_combined.loc[df_combined['name_product'] == 'قهوه ساز مدل 2034 مباشی', 'subscription'] = True
# تغییر یک سلول ستون با اندیس سطر و ستون
#digikala
df_combined.loc[10, 'subscription'] = True
df_combined.loc[11, 'subscription'] = True
df_combined.loc[12, 'subscription'] = True
df_combined.loc[13, 'subscription'] = True
df_combined.loc[14, 'subscription'] = True
#olfa
df_combined.loc[21, 'subscription'] = True
df_combined.loc[22, 'subscription'] = True
df_combined.loc[23, 'subscription'] = True
df_combined.loc[24, 'subscription'] = True

#change to toman
#df_combined['price_product'] =284.24* 60000
#df_combined.loc[1, ' price_product'] =781.01* 60000
#df_combined.loc[2, ' price_product'] =284.24* 60000
#df_combined.loc[3, ' price_product'] =33.11* 60000
#df_combined.loc[4, ' price_product'] =284.24 * 60000



