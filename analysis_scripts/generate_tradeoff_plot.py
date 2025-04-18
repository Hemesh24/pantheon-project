import matplotlib.pyplot as plt

# Simulated average RTT and Throughput
protocols = ['Cubic', 'BBR', 'Copa']
avg_rtt = [110, 80, 50]          # ms
avg_throughput = [9000, 12000, 10000]  # kbps

plt.scatter(avg_rtt, avg_throughput, s=100)

for i, name in enumerate(protocols):
    plt.text(avg_rtt[i] + 1, avg_throughput[i], name)

plt.xlabel('Average RTT (ms) → Lower is better')
plt.ylabel('Average Throughput (kbps) ↑ Higher is better')
plt.title('Throughput vs RTT Trade-off')
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/tradeoff.png')
print("Saved: graphs/tradeoff.png")
