import matplotlib.pyplot as plt
import numpy as np

# Simulated throughput for demo purposes (replace with parsed log later)
time = np.arange(0, 60)
cubic = np.random.normal(8000, 500, 60)
bbr = np.random.normal(12000, 300, 60)
copa = np.random.normal(10000, 400, 60)

plt.plot(time, cubic, label='Cubic')
plt.plot(time, bbr, label='BBR')
plt.plot(time, copa, label='Copa')
plt.xlabel('Time (s)')
plt.ylabel('Throughput (kbps)')
plt.title('Throughput Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/throughput.png')
print("Saved: graphs/throughput.png")
