# Python code to print data and save the visualization

import matplotlib.pyplot as plt
import sqlite3

# connect to SQLite database
conn = sqlite3.connect("pipeline-data.db")
cursor = conn.cursor()

# initilize lists
flow = []
pressure = []
timestamps = []

leak_timestamps = []
leak_flow = []
leak_pressure = []

# print database
print("Pipeline data:")
print("(time (s), flow (L/s), pressure (kPa), leaked)")
cursor.execute("SELECT * FROM PIPELINE")
for row in cursor.fetchall():
  print(row) # print row
  
  # store each cell in different lists
  timestamps.append(row[0]) # 0 = time
  flow.append(row[1]) # 1 = flow
  pressure.append(row[2]) # 2 = pressure

  if row[3] == 'true':
    leak_timestamps.append(row[0]) # 0 = time
    leak_flow.append(row[1]) # 1 = flow
    leak_pressure.append(row[2]) # 2 = pressure


# visualization
fig, ax = plt.subplots(2) # two subplots

ax[0].set_title("Sensor Data Simulation") # title

# Time vs Flow plot
ax[0].plot(timestamps, flow, label="Flow (L/s)", color="blue")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Flow (L/s)")
ax[0].grid(True)

# Time vs Pressure plot
ax[1].plot(timestamps, pressure, label="Pressure (kPa)", color="green")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Pressure (kPa)")
ax[1].grid(True)

# mark leaks
ax[0].scatter(leak_timestamps, leak_flow, color="red", marker="o", s=100, label="Detected Leak")
ax[1].scatter(leak_timestamps, leak_pressure, color="red", marker="o", s=100, label="Detected Leak")

# display plot
plt.tight_layout()
plt.savefig("pipeline_chart.png")
print("Chart saved as pipeline_chart.png")

# close connection
conn.close()