import pandas as pd
import numpy as np


data = pd.read_csv("SolarPrediction.csv")
import re
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import optuna
import xgboost as xgb
import joblib

data['Month'] = data['Data'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
data['Day'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\/)', x).group(0)).astype(np.int)
data['Year'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\s)', x).group(0)).astype(np.int)
data = data.drop('Data', axis=1)

data['Hour'] = data['Time'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
data['Minute'] = data['Time'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)
data['Second'] = data['Time'].apply(lambda x: re.search(r'\d+$', x).group(0)).astype(np.int)

data = data.drop('Time', axis=1)

data['SunriseHour'] = data['TimeSunRise'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
data['SunriseMinute'] = data['TimeSunRise'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

data['SunsetHour'] = data['TimeSunSet'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
data['SunsetMinute'] = data['TimeSunSet'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

data = data.drop(['TimeSunRise', 'TimeSunSet'], axis=1)

data = data.drop(['Year', 'SunriseHour'], axis=1)

y = data['Radiation'].copy()
X = data.drop('Radiation', axis=1).copy()


data = data[data["Month"] == 9]
data = [['Day',"Temperature","Pressure","Humidity","Speed","WindDirection(Degrees)"]]
data = pd.DataFrame(data)
data = data.groupby('Day')['Temperature',"Pressure","Humidity",'Speed','WindDirection(Degrees)'].mean().round(2)
# data = data.loc[(data["Day"] == 1) & (data["Day"] == 20)]
print(data)
