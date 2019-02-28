# import necessary libraries
from flask import Flask, render_template

#Imports all dependencies
import pandas as pd
import datetime
import json
import requests
from pprint import pprint
from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date 
import pymysql
pymysql.install_as_MySQLdb()
Base = declarative_base()
import sqlite3
from sqlalchemy.orm import Session

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/CoreListReports")
def CoreListReports():

    return render_template('corelistreports.html')

@app.route('/supportfilesecon')
def econsupportfiles():

    #Creates the connection to the SQL File
    conn = sqlite3.connect('gfc_data.sqlite')
    engine = create_engine('sqlite:///gfc_data.sqlite')
    session = Session(engine)

    #Shows the class ids for all classes
    class_id = ['econ_unemployment', "econ_new_orders", 'econ_non_defense_x_air', 'econ_capacity_utilization', 'econ_data_initial_claims', 'econ_data_weekly_earnings']

    #Creates the dataframe for all data showing the last 10 observations
    df = pd.read_sql("SELECT * FROM " + class_id[4]+ " ORDER BY id DESC LIMIT 10", conn)
    df['Unemployment Date'] = pd.read_sql("SELECT date FROM " + class_id[0] + " ORDER BY id DESC LIMIT 10", conn)
    df['Unemployment Rate'] = pd.read_sql("SELECT Unemployment_Rate FROM " + class_id[0]+ " ORDER BY id DESC LIMIT 10", conn)
    df['New orders Date'] = pd.read_sql("SELECT date FROM " + class_id[1]+ " ORDER BY id DESC LIMIT 10", conn)
    df['New Capital Goods Orders'] = pd.read_sql("SELECT Value_of_Manufactuters_New_Orders FROM " + class_id[1]+ " ORDER BY id DESC LIMIT 10", conn)
    df['Cap Goods Date'] = pd.read_sql("SELECT date FROM " + class_id[2] + " ORDER BY id DESC LIMIT 10", conn)
    df['Capital Goods x Defense Aircraft New Orders'] = pd.read_sql("SELECT Manufacturers_New_Orders_Non_Defense_Cap_Goods_x_Air FROM " + class_id[2] + " ORDER BY id DESC LIMIT 10", conn)
    df['Utilization Date'] = pd.read_sql("SELECT date FROM " + class_id[3] + " ORDER BY id DESC LIMIT 10", conn)
    df['Factory Utilization Rate'] = pd.read_sql("SELECT Capacity_Utilization_Manufacturing FROM " + class_id[3] + " ORDER BY id DESC LIMIT 10", conn)
    df['Weekly Earnings Date'] = pd.read_sql("SELECT date FROM " + class_id[5] + " ORDER BY id DESC LIMIT 10", conn)
    df['Average Weekly Earnings'] = pd.read_sql("SELECT Average_Weekly_Earnings FROM " + class_id[5] + " ORDER BY id DESC LIMIT 10", conn)
    df = df.drop(columns=['id'])
    df = df.rename(index=str, columns={'Average_Weekly_Initial_Claims': 'Average Weekly Initial Claims', 'date': 'Initial Claims Date'})

    return render_template('supportfilesecon.html', data=df.to_html(index=False, classes='table table-hover table-condensed'))


if __name__ == "__main__":
    app.run(debug=True)