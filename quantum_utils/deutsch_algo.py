from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def create_deutsch_circuit(oracle_circuit):
    """
    Wraps an oracle into the Deutsch Algorithm template.
    1. Prepares auxiliary qubit in |-> state.
    2. Applies Hadamard to input.
    3. Queries Oracle.
    4. Measures input in X-basis.
    """
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(qr, cr)

    # Initialize auxiliary qubit to |->
    qc.x(qr[1])
    qc.h(qr[1])

    # Superposition of input qubit
    qc.h(qr[0])

    # Apply the oracle
    qc.append(oracle_circuit, [qr[0], qr[1]])

    # Basis change back to Z for measurement
    qc.h(qr[0])
    qc.measure(qr[0], cr[0])

    return qc