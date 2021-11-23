from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float 
import pandas as pd
from IPython.display import HTML


# rds_connection_string = "postgres:postgres@localhost:5432/restaurants_db"
# engine = create_engine(f'postgresql://{rds_connection_string}')
# topten_data = pd.read_sql_query('select * from topten', con=engine)
# restaurant_data = pd.read_sql_query('select * from az_restaurants', con=engine)
restaurant_data = pd.read_csv("Flask/static/data/az_yelp_restaurants.csv")
topten_data = pd.read_csv("Flask/static/data/top10_restaurants.csv")


# Create an instance of Flask
app = Flask(__name__)


### Home Page and Rerouting ###
@app.route("/")
def home():
    data_html = HTML(topten_data.to_html(index=False,classes='table table-dark table-striped'))
    restaurant_df = pd.DataFrame(restaurant_data.groupby(['city'])['stars'].count().reset_index())
    # Return template and data
    return render_template("/index.html", topten = data_html,restaurant_data=restaurant_data,restaurant_df=restaurant_df)

@app.route("/index.html")
def returnhome():

    data_html = HTML(topten_data.to_html(index=False,classes='table table-dark table-striped'))
    restaurant_df = pd.DataFrame(restaurant_data.groupby(['city'])['stars'].count().reset_index())
    # Return template and data
    return render_template("/index.html", topten = data_html,restaurant_data=restaurant_data,restaurant_df=restaurant_df)

### Data Model Pages #
@app.route("/logisticRegression.html")
def datamodel_linearRegression():
    return render_template("/logisticRegression.html")

@app.route("/randomForest.html")
def datamodel_randomForest():
    return render_template("/randomForest.html")

@app.route("/neuralNetworks.html")
def datamodel_neuralNetworks():
    return render_template("/neuralNetworks.html")

@app.route("/comparison.html")
def comparison():
    return render_template("/comparison.html")

@app.route("/data.html")
def data():
    return render_template("/data.html")


if __name__ == "__main__":
    app.run(debug=True)

