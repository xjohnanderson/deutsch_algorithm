from qiskit import QuantumCircuit

def constant_oracle(value):
    """
    Creates a constant oracle (f(x) = 0 or f(x) = 1).
    Args:
        value (int): The constant result (0 or 1).
    """
    oracle = QuantumCircuit(2, name=f"Uf_const_{value}")
    if value == 1:
        oracle.x(1)
    return oracle

def balanced_oracle(func_type):
    """
    Creates a balanced oracle (f(0)!=f(1)).
    Args:
        func_type (str): 'x' (identity) or 'not_x' (bit flip).
    """
    oracle = QuantumCircuit(2, name=f"Uf_bal_{func_type}")
    if func_type == 'x':
        oracle.cx(0, 1)
    elif func_type == 'not_x':
        oracle.x(0)
        oracle.cx(0, 1)
        oracle.x(0)
    return oracle