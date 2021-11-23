import pandas as pd
import os


col_names = [
    'Id',
    'Date',
    'Title',
    'Content',
    'Author',
    'Status'
]


df1 = pd.read_csv(r'upload_soon.csv', names=col_names)
df2 = pd.read_csv(r'uploaded.csv', names=col_names)


print(df1.head())
print(df2.head())


for row in df1.index:   
    print('Die Reihe', df1['Id'][row], 'wurde kopiert')
    print(df1['Id'][row], df1['Date'][row], df1['Title'][row], df1['Content'][row], df1['Status'][row])


df1.to_csv('uploaded.csv', mode='a', header='false')

os.remove('upload_soon.csv')


df2 = pd.read_csv(r'uploaded.csv', names=col_names)
print(df2.head())
