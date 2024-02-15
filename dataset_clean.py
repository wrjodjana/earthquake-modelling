import pandas as pd

df = pd.read_csv('earthquake-data.csv')
translations = {
    'tgl': 'Date',
    'ot' : 'Origin Time',
    'lat' : 'Latitude',
    'lon' : 'Longitude',
    'depth' : 'Depth',
    'mag' : 'Magnitude',
    'remark' : 'Remark',
}
df.rename(columns = translations, inplace = True)

# Dropping columns we don't need
temp = df.drop(columns = ['strike1', 'dip1', 'rake1', 'strike2', 'dip2', 'rake2'])
df = temp

# Droping Nan Rows
df.dropna(inplace=True)
