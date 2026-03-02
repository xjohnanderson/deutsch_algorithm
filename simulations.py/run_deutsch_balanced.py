from qiskit_aer import AerSimulator
from qiskit import transpile
from quantum_utils import balanced_oracle, create_deutsch_circuit

def simulate_balanced_cases():
    simulator = AerSimulator()
    test_cases = ['x', 'not_x']
    
    for func_type in test_cases:
        print(f"\n--- Testing Balanced Oracle f(x) = {func_type} ---")
        
        # Build the circuit
        oracle = balanced_oracle(func_type)
        circuit = create_deutsch_circuit(oracle)
        
        # Transpile and Run
        compiled = transpile(circuit, simulator)
        job = simulator.run(compiled, shots=1024)
        counts = job.result().get_counts()
        
        print(circuit)
        print(f"Results: {counts}")
        print("Verification: '1' means Balanced (Correct!)" if '1' in counts else "Error!")

if __name__ == "__main__":
    simulate_balanced_cases()