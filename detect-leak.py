import matplotlib.pyplot as plt
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

# initializing multiple lists
flows = []
leak_indices = []
pressures = []
timestamps = []

for i in range(50): # range(decisecond)
  flow = random.uniform(5, 10) # in L/s
  pressure = random.uniform(200, 300) # in kPa

  if random.random() < 0.2:
    flow -= random.uniform(1, 3)
    pressure -= random.uniform(50, 100)

  flows.append(flow)
  pressures.append(pressure)

  # to store results in deciseconds
  time.sleep(0.1)
      
  if flow < 5 or pressure < 200:
    leak_indices.append(i)
    print(f"[ALERT] Leak detected! Flow = {flow:.2f} L/s, Pressure = {pressure:.2f} kPa")
    print("Sending alert to maintenance team...")
  
  i += 1
  timestamps.append(i/10)

leak_timestamps = [timestamps[i] for i in leak_indices]
leak_flows = [flows[i] for i in leak_indices]
leak_pressures = [pressures[i] for i in leak_indices]

# Visualization

# Two subplots
fig, ax = plt.subplots(2)

# Title
ax[0].set_title("Sensor Data Simulation")

# Time vs Flow plot
ax[0].plot(timestamps, flows, label="Flow (L/s)", color="blue")
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Flow (L/s)")
ax[0].grid(True)

# Time vs Pressure plot
ax[1].plot(timestamps, pressures, label="Pressure (kPa)", color="green")
ax[1].set_xlabel("Time (s)")
ax[1].set_ylabel("Pressure (kPa)")
ax[1].grid(True)

# Mark leaks
if leak_indices:
  ax[0].scatter(leak_timestamps, leak_flows, color="red", marker="o", s=100, label="Detected Leak")
  ax[1].scatter(leak_timestamps, leak_pressures, color="red", marker="o", s=100, label="Detected Leak")

plt.tight_layout()
plt.show()