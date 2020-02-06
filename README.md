# Titanic and Flask

This repository contains code to build a random forest model and deploy as a web service in Flask application. We use the so well known _Titanic_ dataset. 

## Launching the app

- Clone repository to your local machine: `git clone git@github.com:leschiffres/titanic_and_flask.git`

## Using Docker 
 
- Open a terminal.
- Path into the app folder `cd titanic_and_flask`
- Build the image: `docker build -t titanic_app .`
- Start the container: `docker run --rm -p 9001:9000 titanic_app`
- Open a browser and go to the address `http://localhost:9001/`

## Using existing python

In order for the app to be able to run in the host machine,_pandas_, _numpy_, _flask_, _sklearn_ have to be in the list of installed libraries. Then: 

- Open a terminal.
- Path into the app folder `cd titanic_and_flask/app/`.
- Start the flask application by using the command `python3 app.py`.
- Open a browser and go to the address `http://localhost:9000/`

## Files Description

## Root 

- Dockerfile:
- request.py: Uses a service of the flask application, by sending some data of a passenger in json format, and receives the probability of survival.

## Building Model Folder

This folder contains everything regarding the building of the random forest model used in the app.

- *dataset* : Contains the well known titanic dataset that can be found here: https://www.kaggle.com/c/titanic/data
- *titanic_preprocessing_ml.ipynb* : Contains all the code for the preprocessing of the data, building of the model and storing the random forest model into a pickle file.
- *titanic_predict.ipynb* : Reads the test.csv data and produces a prediction of survival. It is not needed for the app but I put it here anyway.
  

## App Folder

It contains all the files building the flask application. 

- mapping.py: Maps given values into numbers (based on the mapping that was done during the preprocessing) so that the random forest model can be used accordingly.
- app.py: Launches the flask application. This is the core of the web app.
