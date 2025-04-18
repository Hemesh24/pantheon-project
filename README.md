# pantheon-project# Pantheon Congestion Control Evaluation

This repo includes:
- Results for CUBIC, BBR, Copa
- Analysis scripts for graphs
- Shell script to automate test runs
- Final report

# Pantheon Congestion Control Evaluation

This repository contains the full setup, experimentation, and analysis for evaluating congestion control algorithms using the [Pantheon](https://github.com/StanfordSNR/pantheon) testbed and [Mahimahi](https://github.com/ravinet/mahimahi) network emulation tools. The work was completed as part of a graduate-level course in Computer Networks.

---

## 📌 Objective

To compare three congestion control protocols — **CUBIC**, **BBR**, and **Copa** — under two network conditions using Pantheon, and analyze their behavior in terms of:
- Throughput
- RTT (Round Trip Time)
- Packet Loss
- Overall performance trade-offs

---

## 🧪 Experiment Scenarios

### 1. Low-Latency / High-Bandwidth
- **50 Mbps bandwidth**
- **10 ms RTT**

### 2. High-Latency / Low-Bandwidth
- **1 Mbps bandwidth**
- **200 ms RTT**

Each experiment ran for **60 seconds**, collecting logs and statistics for later analysis.

---

## 🗂️ Repository Structure

pantheon-project/ ├── analysis_scripts/ │ ├── plot_throughput.py │ ├── plot_rtt.py │ ├── plot_loss.py │ └── generate_tradeoff_plot.py ├── graphs/ │ ├── throughput.png │ ├── rtt.png │ ├── loss.png │ └── tradeoff.png ├── experiments/ │ ├── my_results_50mbps_10ms/ │ └── my_results_1mbps_200ms/ ├── report/ │ └── Roseli_Pantheon_Assignment.docx ├── run_test_scenario.sh └──


---

## ⚙️ How to Reproduce the Results

### 🧾 Requirements

- Linux OS or WSL
- Python 3.x
- Pantheon (cloned from https://github.com/StanfordSNR/pantheon)
- Mahimahi
- Python packages:
  ```bash
  pip3 install matplotlib pandas numpy

 Running the Experiments
Run Pantheon using:

bash
Copy
Edit
bash run_test_scenario.sh my_results_50mbps_10ms
bash run_test_scenario.sh my_results_1mbps_200ms
📊 Generate Graphs from Logs
From the root of the repo, run:

bash
Copy
Edit
python3 analysis_scripts/plot_throughput.py
python3 analysis_scripts/plot_rtt.py
python3 analysis_scripts/plot_loss.py
python3 analysis_scripts/generate_tradeoff_plot.py
This will create .png images in the graphs/ folder, which are embedded in the final report.

📄 Final Report
The completed analysis and discussion of the results are included in:

HemanthFinalReport.docx
