import pandas as pd

col_names = [
    'id',
    'date',
    'title',
    'content',
    'author',
    'status'
]



df1 = pd.read_csv(r'to_upload.csv')
df2 = pd.read_csv(r'uploaded.csv')


print(df1.head())
print(df2.head())

#for line in df1:
#    print(line)