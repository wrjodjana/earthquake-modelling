import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import geopandas as gpd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

from imblearn.combine import SMOTEENN


# earthquake data
df = pd.read_csv('datasets/earthquake-data.csv')

# boundaries data
boundaries = gpd.read_file('datasets/indonesia_boundaries.geojson')
print(boundaries.geometry)

boundaries.plot()
plt.show()



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

# dropping NaN values
df.dropna(inplace=True)

# convert dates to datetime type
df['Date'] = pd.to_datetime(df['Date'])
