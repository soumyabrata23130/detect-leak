# Name: Pipeline Health Checker
# Python program to simulate an IoT pipeline leak detection system.
# Event: IoTricity Season 2
# Team: Tech Warriors
# Members: Soumyabrata Bhattacharjee (lead, CSE 3rd year), Souvik Roy (CSE 3rd year), Sudipta Dolay (EE 3rd year)
# Date: 30 August-1 September, 2025

from datetime import datetime
import random
import sqlite3


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

if ph < 6.5:
  print(f"[ALERT] Acidic water! pH = {ph:.2f}")
  print("Sending alert to water supply team...")
elif ph > 7.5:
  print(f"[ALERT] Alkaline water! pH = {ph:.2f}") 
  print("Sending alert to water supply team...")
else:
  print(f"Normal water. pH = {ph:.2f}")


# connect to SQLite database
conn = sqlite3.connect("pipeline-data.db")
cursor = conn.cursor()

# if table does not exists, create a new one
cursor.execute("CREATE TABLE IF NOT EXISTS PIPELINE(TIME REAL, FLOW REAL, PRESSURE REAL, LEAKED TEXT)")

# sample range for this program, in deciseconds
sample_range = 50

flow = random.uniform(5, 10) # in L/s
pressure = random.uniform(200, 300) # in kPa
now = datetime.now()
timestamp = now.timestamp()

if random.random() < 0.2:
  flow -= random.uniform(1, 2)
  pressure -= random.uniform(50, 100)

leaked_status = "" # to store the leaked status in database

if flow < 5 or pressure < 200:
  leaked_status = "true"
  print(f"[ALERT] Leak detected! Flow = {flow:.2f} L/s, Pressure = {pressure:.2f} kPa")
  print("Sending alert to maintenance team...")
else:
  leaked_status = "false"

# insert pipeline data into database
cursor.execute(f"INSERT INTO PIPELINE VALUES ({timestamp:.0f}, {flow:.2f}, {pressure:.2f}, '{leaked_status}')")


# commit changes and close connection
conn.commit()
conn.close()