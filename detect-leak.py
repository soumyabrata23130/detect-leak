# Python program to simulate an IoT pipeline leak detection system.
# Event: IoTricity Season 2
# Team: Tech Warriors
# Members: Soumyabrata Bhattacharjee (lead, CSE 3rd year), Souvik Roy (CSE 3rd year), Sudipta Dolay (EE 3rd year)
# Date: 30 August-1 September, 2025

import matplotlib.pyplot as plt
import numpy as np
import random
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
if ph < 5:
  print(f"[ALERT] Corrosive water! pH = {ph:.2f}")
  print("Sending alert to water supply team...")
elif ph > 9:
  print(f"[ALERT] Alkaline water! pH = {ph:.2f}") 
  print("Sending alert to water supply team...")
else:
  print(f"Normal water. pH = {ph:.2f}")

sample_range = 50 # sample range for this program, in deciseconds

# initializing multiple lists
flow = np.random.uniform(5, 10, sample_range) # in L/s
pressure = np.random.uniform(200, 300, sample_range) # in kPa
leak_indices = []
timestamps = np.arange(0, sample_range/10, 0.1) # timestamps from 0 to sample range, in seconds

for i in range(sample_range):
  if random.random() < 0.2:
    flow[i] -= random.uniform(1, 2)
    pressure[i] -= random.uniform(50, 100)

  time.sleep(0.1) # to store results in deciseconds
  
  if flow[i] < 5 or pressure[i] < 200:
    leak_indices.append(i)
    print(f"[ALERT] Leak detected! Flow = {flow[i]:.2f} L/s, Pressure = {pressure[i]:.2f} kPa")
    print("Sending alert to maintenance team...")
  
  i += 1

# Lists for leaks
leak_timestamps = [timestamps[i] for i in leak_indices]
leak_flows = [flow[i] for i in leak_indices]
leak_pressures = [pressure[i] for i in leak_indices]

# Visualization
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

# Mark leaks
if leak_indices:
  ax[0].scatter(leak_timestamps, leak_flows, color="red", marker="o", s=100, label="Detected Leak")
  ax[1].scatter(leak_timestamps, leak_pressures, color="red", marker="o", s=100, label="Detected Leak")

# Display plot
plt.tight_layout()
plt.show()