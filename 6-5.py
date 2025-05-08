import pandas as pd

df = pd.read_csv('listings.csv', index_col='id')

df['last_review'] = pd.to_datetime(df['last_review'])

dsf = df[(df['last_review'].dt.year == 2024) & (df['last_review'].dt.is_month_end)]

dsf[['last_review', 'number_of_reviews']].max()

dsf_w = df[(df['last_review'].dt.year == 2024) & (df['last_review'].dt.dayofweek == 5)]

print(dsf_w['number_of_reviews'].sum())
print(dsf)