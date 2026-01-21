
---

# Deutsch's Algorithm Implementation in Qiskit

This repository contains a modular implementation of **Deutsch's Algorithm**, one of the first examples of a quantum algorithm that outperforms its classical counterpart.

## 📌 Project Overview

Deutsch’s algorithm determines whether a hidden Boolean function  is **constant** (returns the same value for all inputs) or **balanced** (returns 0 for half the inputs and 1 for the other half).

* **Classical complexity**: 2 queries to the function.
* **Quantum complexity**: 1 query to the function.

## 📂 Directory Structure

```text
deutsch_algorithm/
├── src/
│   ├── oracles.py           # Logic for Constant and Balanced oracles
│   └── deutsch_circuit.py   # The main Deutsch algorithm framework
├── scripts/
│   ├── run_deutsch.py       # Main simulation script for all cases
│   └── run_entanglement.py  # Standalone script for Bell state testing
└── requirements.txt         # Project dependencies

```

---

## 🚀 Getting Started

### 1. Installation

Ensure you have Python 3.8+ installed. Install the necessary quantum computing libraries:

```bash
pip install qiskit qiskit-aer matplotlib

```

### 2. Running the Simulation

To execute the Deutsch algorithm across all four oracle types (Constant 0, Constant 1, Balanced , and Balanced ), run:

```bash
python scripts/run_deutsch.py

```

---

## 🧬 How it Works

The algorithm utilizes **Phase Kickback** to encode the function's property into the phase of the input qubit.

1. **Initialization**: The auxiliary qubit is put into the  state using  and  gates.
2. **Superposition**: The input qubit is put into the  state.
3. **The Oracle ()**: The function is applied. Due to the  state on the target, the output  is "kicked back" as a phase:

4. **Interference**: A final Hadamard gate is applied to the input qubit.
* If  is **constant**, the result is .
* If  is **balanced**, the result is .



---

## 📊 Expected Results

When running the scripts, your measurement counts should look like this:

| Oracle Type | Function | Expected Measurement |
| --- | --- | --- |
| **Constant** |  | `{'0': 1024}` |
| **Constant** |  | `{'0': 1024}` |
| **Balanced** |  | `{'1': 1024}` |
| **Balanced** |  | `{'1': 1024}` |

---

