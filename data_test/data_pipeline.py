import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import requests
import json

def fetch_data_from_file():
       df=pd.read_csv('combined.csv')
       return process_data(df)

def process_data(df):
       df = df.drop_duplicates(keep="first")
       mpg = df[df['model'] == ' C Class']['mpg'].mean()
       df.loc[(df['mpg'].isna()) & (df['model'] == ' C Class'), 'mpg'] = mpg
       tax = df[df['model'] == ' C Class']['tax'].mean()
       df.loc[(df['tax'].isna()) & (df['model'] == ' C Class'), 'tax'] = tax
       mpg = df[df['model'] == ' Focus']['mpg'].mean()
       df.loc[(df['mpg'].isna()) & (df['model'] == ' Focus'), 'mpg'] = mpg
       tax = df[df['model'] == ' Focus']['tax'].mean()
       df.loc[(df['tax'].isna()) & (df['model'] == ' Focus'), 'tax'] = tax
       le = preprocessing.LabelEncoder()
       le.fit(df['company'])
       df['companyLE'] = le.transform(df['company'])
       le = preprocessing.LabelEncoder()
       le.fit(df['model'])
       df['modelLE'] = le.transform(df['model'])
       # le = preprocessing.LabelEncoder()
       # le.fit(df['transmission'])
       # df['transmissionLE']=le.transform(df['transmission'])
       df_temp = pd.get_dummies(df['transmission'])
       df_temp.columns = ['transmission_' + col for col in df_temp.columns]
       df = df.join(df_temp)
       # df=df.join(pd.get_dummies(df['fuelType']))
       df_temp = pd.get_dummies(df['fuelType'])
       df_temp.columns = ['fuelType_' + col for col in df_temp.columns]
       df = df.join(df_temp)
       X = df[['year', 'mileage', 'engineSize', 'companyLE', 'modelLE',
               'transmission_Automatic', 'transmission_Manual', 'transmission_Other',
               'transmission_Semi-Auto', 'fuelType_Diesel', 'fuelType_Electric',
               'fuelType_Hybrid', 'fuelType_Other', 'fuelType_Petrol']]
       y = df['price']
       X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
       return X_train, X_test, y_train, y_test


def fetch_data_from_mongo():
       r = requests.get('http://192.168.1.132:5000/car_data')
       if r.status_code == 200:
              df = pd.DataFrame(json.loads(r.text))
              return process_data(df)
       else:
              raise