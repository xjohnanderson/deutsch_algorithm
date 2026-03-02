from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

def run_bell_experiment():
    # 1. Setup Circuit
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, cr)

    # 2. Entangle (Bell State |phi+>)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])

    # 3. Apply Phase Flip and Basis Change
    qc.z(qr[0])     # Phase Flip
    qc.h(qr[0])     # Change to X-basis
    qc.h(qr[1])     # Change to X-basis

    # 4. Measure
    qc.measure(qr, cr)

    # 5. Simulate
    simulator = AerSimulator()
    compiled = transpile(qc, simulator)
    counts = simulator.run(compiled, shots=1024).result().get_counts()

    print("Quantum Circuit for Entangled State (X-Basis):")
    print(qc)
    print(f"\nMeasurement Results: {counts}")

if __name__ == "__main__":
    run_bell_experiment()