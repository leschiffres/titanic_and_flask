import requests
import pandas as pd

df = pd.read_csv('dataset/train.csv')

passenger_id = 89
# passenger = df.loc[df['PassengerId']==passenger_id, ['Name', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
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

print(dc)

url = 'http://localhost:5001/results'

r = requests.post(url, json=dc)

print(r.json())