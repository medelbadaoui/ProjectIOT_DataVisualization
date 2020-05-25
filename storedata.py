# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:20:00 2020

@author: ENGINEER
"""
import json
import sqlite3

DB_Name= "Iot_Database.db"


class DatabaseManager():
    def __init__(self):
        self.conn=sqlite3.connect(DB_Name,isolation_level=None)
        self.cur=self.conn.cursor()
        
    def add_del_update_db_record(self,sql_query,args=()):
        self.cur.execute(sql_query,args)
        return
    def select_db_record(self,sql_query,args=()):
        self.cur.execute(sql_query,args)
        return self.cur.fetchall();
    def __del__(self):
        self.cur.close()
        self.conn.close()
    @staticmethod
    def getDataSet(sqlText):
        dbObj=DatabaseManager()
        rows=dbObj.select_db_record(sqlText)
        del dbObj
        return rows 
    
    
def Temperature_Data_Handler(jsonData):
    
    json_Dict=json.loads(jsonData)
    SensorID=json_Dict['Sensor_ID']
    Date_Time=json_Dict['Date']
    Temperature=float(json_Dict['Temperature'])
    TemperatureLevel=json_Dict['TemperatureLevel']
    

    dbObj=DatabaseManager()
    dbObj.add_del_update_db_record("insert into Temperature_Data(SensorID,Date_Time,Temperature,TemperatureLevel) values (?,?,?,?)",
                                   [SensorID,Date_Time,Temperature,TemperatureLevel])
    del dbObj
    print("Inserted Temperature to Database")
    print("")
    
def Humidity_Data_Handler(jsonData):
    json_Dict=json.loads(jsonData)
    SensorID=json_Dict['Sensor_ID']
    Date_Time=json_Dict['Date']
    Humidity=float(json_Dict['Humidity'])
    HumidityLevel=json_Dict['HumidityLevel']

    dbObj=DatabaseManager()
    dbObj.add_del_update_db_record("insert into Humidity_Data(SensorID,Date_Time,Humidity,HumidityLevel) values (?,?,?,?)",
                                   [SensorID,Date_Time,Humidity,HumidityLevel])
    del dbObj
    print("Inserted Humidity to Database")
    print("")

def Acceleration_Data_Handler(jsonData):
    json_Dict=json.loads(jsonData)
    SensorID=json_Dict['Sensor_ID']
    Date_Time=json_Dict['Date']
    print('**************',Date_Time)
    accX=float(json_Dict['accX'])
    accY=float(json_Dict['accY'])
    accZ=float(json_Dict['accZ'])
    dbObj=DatabaseManager()
    dbObj.add_del_update_db_record('insert into Acceleration_Data(SensorID,Date_Time,accX,accY,accZ) values (?,?,?,?,?)',[SensorID,Date_Time,accX,accY,accZ])
    del dbObj
    print("Inserted Accelerator to Database")
    print("")
    
def sensor_Data_Handler(Topic,jsonData):
    if Topic=="Home/BedRoom/DHT1/Temperature":
        Temperature_Data_Handler(jsonData)
    elif Topic=="Home/BedRoom/DHT1/Humidity":
        Humidity_Data_Handler(jsonData)
    elif Topic=="Home/BedRoom/DHT1/Acceleration":
        Acceleration_Data_Handler(jsonData)

limit=10
def Temperature_Data_Getter():
    dbObj=DatabaseManager()
    numberofrecords=dbObj.select_db_record('SELECT count(*) FROM Temperature_Data')
    num=numberofrecords[0][0]
    
    return dbObj.select_db_record('SELECT * FROM Temperature_Data LIMIT '+str(limit)+' OFFSET ' +str(num-limit))
    
def Humidity_Data_Getter():
    dbObj=DatabaseManager()
    numberofrecords=dbObj.select_db_record('SELECT count(*) FROM Humidity_Data')
    num=numberofrecords[0][0]
    return dbObj.select_db_record('SELECT * FROM Humidity_Data LIMIT '+str(limit)+' OFFSET ' +str(num-limit))

def Accelerator_Data_Getter():
    dbObj=DatabaseManager()
    numberofrecords=dbObj.select_db_record('SELECT count(*) FROM Acceleration_Data')
    num=numberofrecords[0][0]
    return dbObj.select_db_record('SELECT * FROM Acceleration_Data LIMIT '+str(limit)+' OFFSET ' +str(num-limit))
def get_Humidity_Level(level):
    dbObj=DatabaseManager()
    number=dbObj.select_db_record("SELECT count(*) FROM Humidity_Data where HumidityLevel='"+level+"'")
    return number[0][0]
def get_Temperature_Level(level):
    dbObj=DatabaseManager()
    number=dbObj.select_db_record("SELECT count(*) FROM Temperature_Data where TemperatureLevel='"+level+"'")
    return number[0][0]    
def sensor_Data_Getter(Topic):
    if Topic == "Home/Bedroom/DHT1/Temperature":
        return Temperature_Data_Getter()
    elif Topic=="Home/Bedroom/DHT1/Humidity":
        return Humidity_Data_Getter()
    elif Topic=="Home/Bedroom/DHT1/Acceleration":
        return Accelerator_Data_Getter()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    