import pandas as pd

name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
          }

df = pd.DataFrame(name_dict)

print (df)
df.to_csv('data_file.csv', index= False)