# Name: Pipeline Health Checker
# Python program to simulate an IoT pipeline leak detection system.
# Event: IoTricity Season 2
# Team: Tech Warriors
# Members: Soumyabrata Bhattacharjee (lead, CSE 3rd year), Souvik Roy (CSE 3rd year), Sudipta Dolay (EE 3rd year)
# Date: 30 August-1 September, 2025

import numpy as np
import random
import sqlite3
import time


# age of pipeline
age = random.uniform(0, 10)

if random.random() < 0.2:
  age += random.uniform(4, 16)

if age > 10:
  print(f"[ALERT] Old pipeline! Age = {age:.0f} years")
  print("Sending alert to maintenance team...")
else:
  print(f"Age of pipeline = {age:.0f} years")


# pH of water
ph = random.uniform(2, 12)

if ph < 6:
  print(f"[ALERT] Acidic water! pH = {ph:.2f}")
  print("Sending alert to water supply team...")
elif ph > 8:
  print(f"[ALERT] Alkaline water! pH = {ph:.2f}") 
  print("Sending alert to water supply team...")
else:
  print(f"Normal water. pH = {ph:.2f}")


# connect to SQLite database
conn = sqlite3.connect("pipeline-data.db")
cursor = conn.cursor()


# if table exists drop it, else create a table
cursor.execute("DROP TABLE IF EXISTS PIPELINE")
cursor.execute("CREATE TABLE IF NOT EXISTS PIPELINE(TIME REAL, FLOW REAL, PRESSURE REAL, LEAKED TEXT)")


# sample range for this program, in deciseconds
sample_range = 50


# initialize multiple lists
flow = np.random.uniform(5, 10, sample_range) # in L/s
pressure = np.random.uniform(200, 300, sample_range) # in kPa
timestamps = np.arange(0, sample_range/10, 0.1) # timestamps from 0 to sample range, in seconds
leak_indices = []


# to print multiple leak alerts and store both normal and leaked data
for i in range(sample_range):
  if random.random() < 0.2:
    flow[i] -= random.uniform(1, 2)
    pressure[i] -= random.uniform(50, 100)

  time.sleep(0.1) # to store results in deciseconds
  leaked_status = "" # to store the leaked status in database
  
  if flow[i] < 5 or pressure[i] < 200:
    leaked_status = "true"
    leak_indices.append(i)
    print(f"[ALERT] Leak detected! Flow = {flow[i]:.2f} L/s, Pressure = {pressure[i]:.2f} kPa")
    print("Sending alert to maintenance team...")
  else:
    leaked_status = "false"
  
  # insert pipeline data into database
  cursor.execute(f"INSERT INTO PIPELINE VALUES ({timestamps[i]:.1f}, {flow[i]:.2f}, {pressure[i]:.2f}, '{leaked_status}')")


# commit changes and close connection
conn.commit()
conn.close()