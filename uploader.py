import pandas as pd
import os
import json


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


for row in df1.index:
    post = {
        'date': df1['Date'][row],
        'title': df1['Title'][row],
        'content': df1['Content'][row],
        'status': df1['Status'][row]
    }

    print(df1['Title'][row], 'published.')


print('All Articles have been published.')


df_t = pd.read_csv(r'upload_soon.csv')
df_t.to_csv('uploaded.csv', mode='a', index=0)
print('Appended Old CSV File to Archive.')

#os.remove('upload_soon.csv')
print('Deleted Old CSV File.')


df2 = pd.read_csv(r'uploaded.csv', names=col_names, skiprows=[0])
#print(df2.head(150))
