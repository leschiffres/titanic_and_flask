from flask import Flask, request, jsonify, render_template
import pickle
import mapping as m

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    dc = {'Name': 'John, Mr. Douglas', 
    'Pclass':2, 
    'Sex': 'Male',
    'Age': '42' ,
    'SibSp': '1' ,
    'Parch': '2' ,
    'Fare': '20.1'}

    return render_template('index.html',
        prediction_text='NaN',
        p_name=dc['Name'],
        p_class=dc['Pclass'],
        p_sex=dc['Sex'],
        p_age=dc['Age'],
        p_sibsp=dc['SibSp'],
        p_parch=dc['Parch'],
        p_fare=dc['Fare'])

# Receives json as input and outputs probability of survival
# This service is activated by an external program (e.g. request.py)
@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    print(data)

    title = m.map_title(data['Name'])
    age_group = m.map_age(data['Age'])
    sex = m.map_sex(data['Sex'])

    age = data['Age']
    pclass = data['Pclass']
    sibsp = data['SibSp']
    parch = data['Parch']

    family_size = m.map_family_size(parch, sibsp)
    is_alone = m.map_is_alone(family_size)

    fare = data['Fare']

    row = [[title, age, age_group, sex, pclass, is_alone, family_size, parch, sibsp, fare]]
    output = model.predict_proba(row)[0][1]
    return jsonify(output)

#
@app.route('/predict',methods=['POST'])
def predict():
    
    name = request.form["passenger_name" ]
    title = m.map_title(name)

    age = float(request.form["passenger_age"])
    age_group = m.map_age(age)

    sex = request.form["passenger_sex"]
    sex = m.map_sex(sex)

    pclass = int(request.form["passenger_class"])

    sibsp = int(request.form["passenger_sibsp"])
    parch = int(request.form["passenger_parch"])
    family_size = m.map_family_size(parch, sibsp)
    is_alone = m.map_is_alone(family_size)

    fare = float(request.form["passenger_fare" ])

    given_data = {
        'Name': request.form["passenger_name" ],
        'Pclass' : int(request.form["passenger_class"]),
        'Sex': request.form["passenger_sex"], 
        'Age': float(request.form["passenger_age"]),
        'SibSp': int(request.form["passenger_sibsp"]), 
        'Parch': int(request.form["passenger_parch"]), 
        'Fare': float(request.form["passenger_fare" ])
    }
    print("Given Data")
    print(given_data)

    data = {
        "title": title, 
        "age": age, 
        "age_group": age_group, 
        "sex": sex, 
        "pclass": pclass, 
        "is_alone": is_alone, 
        "family_size": family_size, 
        "parch": parch, 
        "sibsp": sibsp, 
        "fare":fare
    }
    print("Transformed Data")
    print(data)
    row = [[title, age, age_group, sex, pclass, is_alone, family_size, parch, sibsp, fare]]
    output = model.predict_proba(row)[0][1]

    return render_template('index.html', 
        prediction_text='{}'.format(output),
        p_name=given_data['Name'],
        p_class=given_data['Pclass'],
        p_sex=given_data['Sex'],
        p_age=given_data['Age'],
        p_sibsp=given_data['SibSp'],
        p_parch=given_data['Parch'],
        p_fare=given_data['Fare'])

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001)
