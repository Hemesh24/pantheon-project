import matplotlib.pyplot as plt
import numpy as np

# Simulated RTT values
time = np.arange(0, 60)
cubic = np.random.normal(110, 20, 60)
bbr = np.random.normal(80, 10, 60)
copa = np.random.normal(50, 5, 60)

plt.plot(time, cubic, label='Cubic')
plt.plot(time, bbr, label='BBR')
plt.plot(time, copa, label='Copa')
plt.xlabel('Time (s)')
plt.ylabel('RTT (ms)')
plt.title('RTT Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/rtt.png')
print("Saved: graphs/rtt.png")
