import requests
import pandas as pd
import random

# read data
df = pd.read_csv('./building model/dataset/train.csv')

# find a passenger whose data are complete
passenger_id = random.randint(0, df.shape[0]-1)
passenger = df.iloc[passenger_id - 1]

while pd.isna(passenger['Name']) or pd.isna(passenger['Pclass']) or pd.isna(passenger['Sex']) or pd.isna(passenger['Age']) or pd.isna(passenger['SibSp']) or pd.isna(passenger['Parch']) or pd.isna(passenger['Fare']):
	passenger_id = random.randint(0, df.shape[0]-1)
	passenger = df.iloc[passenger_id - 1]

dc = {
	'Name': str(passenger['Name']), 
	'Pclass': int(passenger['Pclass']), 
	'Sex': str(passenger['Sex']), 
	'Age': float(passenger['Age']), 
	'SibSp': int(passenger['SibSp']), 
	'Parch': int(passenger['Parch']), 
	'Fare': float(passenger['Fare'])
}

print(f'Passenger ID: {passenger_id}')
print(dc)

url = 'http://localhost:5001/results'
# url = 'http://0.0.0.0:5001/results'

r = requests.post(url, json=dc)

print(r.json())