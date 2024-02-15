import pandas as pd

df = pd.read_csv('datasets/earthquake-data.csv')

translations = {
    'tgl': 'Date',
    'ot' : 'Origin Time',
    'lat' : 'Latitude',
    'lon' : 'Longitude',
    'depth' : 'Depth',
    'mag' : 'Magnitude',
    'remark' : 'Location',
}
df.rename(columns = translations, inplace = True)

# Dropping columns we don't need
df_drop = df.drop(['Origin Time', 'Location', 'strike1', 'dip1', 'rake1', 'strike2', 'dip2', 'rake2'], axis=1)
df = df_drop

# Dropping NAN values
df.dropna(inplace=True)

# Handling Outliers
df_numerical = df.iloc[:,1:5]

def remove_outliers(df):
    df_no_outliers = df.copy()
    for i in df_no_outliers.columns:
        Q1 = df_no_outliers[i].quantile(0.25)
        Q3 = df_no_outliers[i].quantile(0.75)
        IQR = Q3-Q1

        upperBound = Q3 + (1.5*IQR) 
        lowerBound = Q1 - (1.5*IQR) 

        df_no_outliers = df_no_outliers[df_no_outliers[i] <= upperBound]
        df_no_outliers = df_no_outliers[df_no_outliers[i] >= lowerBound]

        df_no_outliers = df_no_outliers.reset_index(drop = True)
    return df_no_outliers

df_clean = remove_outliers(df_numerical)
df_comp = df[df.index.isin(df_clean.index)]
df_prediction = df_comp