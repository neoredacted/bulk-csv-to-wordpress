import pandas as pd
import os
import csv

col_names = [
    'id',
    'date',
    'title',
    'content',
    'author',
    'status'
]



df1 = pd.read_csv(r'upload_soon.csv', names=col_names, skiprows=[0])
df2 = pd.read_csv(r'uploaded.csv', names=col_names, skiprows=[0])

print(df1.head())
print(df2.head())


for row in df1.index:   
    print('Die Reihe', df1['Id'][row], 'wurde kopiert')
    print(df1['Id'][row], df1['Date'][row], df1['Title'][row], df1['Content'][row], df1['Status'][row])


df1.to_csv('Z:/projects/bulk-csv-to-wordpress/uploaded.csv', mode='a', header='false')

os.remove('Z:/projects/bulk-csv-to-wordpress/upload_soon.csv')

with open('upload_soon.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(col_names)


df1 = pd.read_csv(r'upload_soon.csv', names=col_names, skiprows=[0])
df2 = pd.read_csv(r'uploaded.csv', names=col_names, skiprows=[0])

print(df1.head())
print(df2.head())
