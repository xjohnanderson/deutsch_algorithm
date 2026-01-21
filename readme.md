
---

# Deutsch's Algorithm Implementation in Qiskit

This repository contains a modular implementation of **Deutsch's Algorithm**, one of the first examples of a quantum algorithm that outperforms its classical counterpart.

## 📌 Project Overview

Deutsch’s algorithm determines whether a hidden Boolean function  is **constant** (returns the same value for all inputs) or **balanced** (returns 0 for half the inputs and 1 for the other half).

* **Classical complexity**: 2 queries to the function.
* **Quantum complexity**: 1 query to the function.

---

## 📊 Data Analysis Key Findings

The following results were obtained from simulating the circuit with 1024 shots per oracle type using the `AerSimulator`:

| Oracle Type | Function | Measurement Result | Classification |
| --- | --- | --- | --- |
| **Constant** |  | `0` (100%) | Constant |
| **Constant** |  | `0` (100%) | Constant |
| **Balanced** |  | `1` (100%) | Balanced |
| **Balanced** |  | `1` (100%) | Balanced |

### 🔍 Analysis Breakdown

* **Constant Functions:** When simulated with oracles  and , the measurement result consistently indicated **'0'**. This demonstrates the algorithm correctly identifies constant functions.
* **Balanced Functions:** For oracles  and , all 1024 shots yielded a **'1'**. This confirms the algorithm correctly identifies balanced functions.
* **Discrimination Capability:** In all tested scenarios, the Deutsch algorithm successfully distinguished between constant and balanced functions by returning '0' for constant and '1' for balanced.

---

## 💡 Insights & Next Steps

* **Quantum Advantage:** The simulations effectively demonstrate the core principle of the Deutsch algorithm, which uses **quantum superposition** and **interference** to determine a global property of a function in a single query.
* **Foundational Logic:** This single-query capability highlights a fundamental quantum advantage. While simple for a 1-bit function, it lays the groundwork for more complex algorithms like **Deutsch-Jozsa** and **Grover’s Algorithm**, which offer significant speedups for larger computational problems.

---

## 📂 Directory Structure

```text
deutsch_algorithm/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── oracles.py           # Logic for Constant and Balanced oracles
│   └── deutsch_circuit.py   # The main Deutsch algorithm framework
├── scripts/
│   ├── run_deutsch.py       # Main simulation script for all cases
│   └── run_entanglement.py  # Standalone script for Bell state testing
└── requirements.txt         # Project dependencies

```

---

## 🚀 Getting Started

1. **Installation:**
```bash
pip install qiskit qiskit-aer

```


2. **Running the Simulation:**
```bash
python scripts/run_deutsch.py

```



---

