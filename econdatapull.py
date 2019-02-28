#imports python modules
import pandas as pd
import datetime
import json
import requests
from pprint import pprint

#Imports all the relevant Modules
from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date 
import pymysql
pymysql.install_as_MySQLdb()
Base = declarative_base()

#Establishes the connection
import sqlite3
conn = sqlite3.connect('gfc_data.sqlite')
engine = create_engine('sqlite:///gfc_data.sqlite')

from sqlalchemy.orm import Session
session = Session(engine)

#Builds the table in the database
class econ_data_unemployment(Base):
    __tablename__ = 'econ_unemployment'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Unemployment_Rate = Column(Float)

class econ_data_new_orders(Base):
    __tablename__ = 'econ_new_orders'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Value_of_Manufactuters_New_Orders = Column(Float)
    
class econ_data_non_defense(Base):
    __tablename__ = 'econ_non_defense_x_air'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Manufacturers_New_Orders_Non_Defense_Cap_Goods_x_Air = Column(Float)
    
class econ_data_utilization(Base):
    __tablename__ = 'econ_capacity_utilization'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Capacity_Utilization_Manufacturing = Column(Float)
    
class econ_data_claims(Base):
    __tablename__ = 'econ_data_initial_claims'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Average_Weekly_Initial_Claims = Column(Float)
    
class econ_data_earnings(Base):
    __tablename__ = 'econ_data_weekly_earnings'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    Average_Weekly_Earnings = Column(Float)
    
#Creates the tables 
Base.metadata.tables
Base.metadata.create_all(engine)

#Imports API Key
api_key = "5ec272d8e55ecfd7543c4dfcc0fdf45d"

#Builds the variables for the for Loop
series_id = ['UNRATE', 'NEWORDER', 'ACOGNO', 'MCUMFN', 'ICSA', 'CES0500000011']
class_id = ['econ_unemployment', "econ_new_orders", 'econ_non_defense_x_air', 'econ_capacity_utilization', 'econ_data_initial_claims', 'econ_data_weekly_earnings']
data = ['Unemployment_Rate', 'Value_of_Manufactuters_New_Orders', 'Manufacturers_New_Orders_Non_Defense_Cap_Goods_x_Air', 'Capacity_Utilization_Manufacturing', 'Average_Weekly_Initial_Claims','Average_Weekly_Earnings']

url_list = []
length_list = []


for series_id in series_id:
    #Creates the Target URL
    data_url = 'https://api.stlouisfed.org/fred/series/observations?series_id=' + series_id + '&api_key=' + api_key + '&file_type=json' 
    responses1 = requests.get(data_url).json()
    length = responses1['count'] 
    url_list.append(data_url)
    length_list.append(length)

#Loops over all the data
unemployment = requests.get(url_list[0]).json()
for j in range(length_list[0]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[0], conn)
    observations = df['id'].max()
    
    if j <= observations:
        continue
    else:
        #Commits if no duplicates  
        table = class_id[0]
        date_output = unemployment['observations'][j]['date']  
        data_output = unemployment['observations'][j]['value']
        output = econ_data_unemployment(date=date_output, Unemployment_Rate=data_output)
        session.add(output)
 
session.commit()

new_orders = requests.get(url_list[1]).json()
for k in range(length_list[1]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[1], conn)
    observations = df['id'].max()
    
    if k <= observations:
        continue
    else: 
        try:
            table = class_id[1]
            date_output = new_orders['observations'][k]['date']
            data_output = new_orders['observations'][k]['value']
            if data_output != '.':
                output = econ_data_new_orders(date=date_output, Value_of_Manufactuters_New_Orders=data_output)
                session.add(output)
            else :
                continue
        except:
            continue
            
session.commit()

cap_goods = requests.get(url_list[2]).json()
for l in range(length_list[2]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[2], conn)
    observations = df['id'].max()
    
    if l <= observations:
        continue
    else:
        try:
            table = class_id[2]
            date_output = cap_goods['observations'][l]['date']
            data_output = cap_goods['observations'][l]['value']
            output = econ_data_non_defense(date=date_output, Manufacturers_New_Orders_Non_Defense_Cap_Goods_x_Air=data_output)
            session.add(output)
        except:
            continue

session.commit()

cap_ut = requests.get(url_list[3]).json()
for m in range(length_list[3]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[3], conn)
    observations = df['id'].max()
    
    if m <= observations:
        continue
    else:
        try:
            table = class_id[3]
            date_output = cap_ut['observations'][m]['date']
            data_output = cap_ut['observations'][m]['value']
            output = econ_data_utilization(date=date_output, Capacity_Utilization_Manufacturing=data_output)
            session.add(output)
        except:
            continue

session.commit()

initial_claims = requests.get(url_list[4]).json()
for n in range(length_list[4]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[4], conn)
    observations = df['id'].max()
    
    if n <= observations:
        continue
    else:
        try:
            table = class_id[4]
            date_output = initial_claims['observations'][n]['date']
            data_output = initial_claims['observations'][n]['value']
            output = econ_data_claims(date=date_output, Average_Weekly_Initial_Claims=data_output)
            session.add(output)
        except:
            continue
            
session.commit()

weekly_earnings = requests.get(url_list[5]).json()
for o in range(length_list[5]):
    #Finds how many observations there are
    df = pd.read_sql("SELECT id FROM " + class_id[5], conn)
    observations = df['id'].max()
    
    if o <= observations:
        continue
    else:
        try:
            table = class_id[5]
            date_output = weekly_earnings['observations'][o]['date']   
            data_output = weekly_earnings['observations'][o]['value']
            output = econ_data_earnings(date=date_output, Average_Weekly_Earnings=data_output)
            session.add(output)
        except:
            continue

session.commit()