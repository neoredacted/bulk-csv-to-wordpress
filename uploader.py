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

    with open("sample.json", "w") as outfile:
        json.dump(post, outfile)
    
    
    print('Die Reihe', df1['Id'][row], 'wurde kopiert')


df_t = pd.read_csv(r'upload_soon.csv')
df_t.to_csv('uploaded.csv', mode='a', index=0)

#os.remove('upload_soon.csv')


df2 = pd.read_csv(r'uploaded.csv', names=col_names, skiprows=[0])
print(df2.head(150))
