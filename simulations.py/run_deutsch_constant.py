from qiskit_aer import AerSimulator
from qiskit import transpile
from quantum_utils import constant_oracle, create_deutsch_circuit

def simulate_constant_cases():
    simulator = AerSimulator()
    
    for val in [0, 1]:
        print(f"\n--- Testing Constant Oracle f(x) = {val} ---")
        oracle = constant_oracle(val)
        circuit = create_deutsch_circuit(oracle)
        
        compiled = transpile(circuit, simulator)
        counts = simulator.run(compiled, shots=1024).result().get_counts()
        
        print(circuit)
        print(f"Results: {counts}")
        print("Verification: '0' means Constant (Correct!)" if '0' in counts else "Error!")

if __name__ == "__main__":
    simulate_constant_cases()

    