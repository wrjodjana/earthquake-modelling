import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from imblearn.combine import SMOTEENN

df = pd.read_csv('earthquake-data.csv')

# added translations
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

# remove unuseful columns
df_drop = df.drop(columns=['strike1', 'dip1', 'rake1', 'strike2', 'rake2'])
df = df_drop
print(df)

# dropping NaN values
df.dropna(inplace=True)

# convert dates to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# time series of earthquakes over the years
plt.figure(figsize =(12,8))
time_series = sns.lineplot(x=df['Date'].dt.year,y="Magnitude",data=df,color="#ffa600")
time_series.set_title("Time Series Of Earthquakes in Indonesia", color="#58508d")
time_series.set_ylabel("Magnitude", color="#58508d")
time_series.set_xlabel("Date", color="#58508d")
plt.show()

# magnitude graphs
plt.figure(figsize=(12,9))
mean_magnitude = df["Magnitude"].mean()
magnitude_plot = sns.distplot(df["Magnitude"].values, color ="#ffa600")
magnitude_plot.set_title("Magnitudes of Earthquakes in Indonesia")
magnitude_plot.set_ylabel("Depth", color="#58508d")
magnitude_plot.set_xlabel("Magnitude", color="#58508d")
plt.show()