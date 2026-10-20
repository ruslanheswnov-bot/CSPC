import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3  # decay constant, given

# TODO 1: read decay_observed.csv
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: set N0 to the first observed value and build analytical
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make the 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))

# Sol qrafik (Müşahidə olunan məlumatlar)
ax1.scatter(t, observed, color='blue', label='Observed Data', s=15)
ax1.set_title("Observed Data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Count")

# Sağ qrafik (Analitik qanun)
ax2.plot(t, analytical, color='red', label='Analytical Law', linewidth=2)
ax2.set_title("Analytical Law")
ax2.set_xlabel("Time")

plt.tight_layout()

# TODO 4: save the figure as figure.png
plt.savefig("figure.png")
print("Grafik ugurla yadda saxlanildi: figure.png")
