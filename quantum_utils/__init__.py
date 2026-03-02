"""
Quantum Utilities Package
A collection of modules for building oracles and 
implementing the Deutsch Algorithm.
"""

# Pulling functions into the package level for easier access
from .oracles import constant_oracle, balanced_oracle
from .deutsch_algo import create_deutsch_circuit

# Define what is available for 'from quantum_utils import *'
__all__ = [
    'constant_oracle',
    'balanced_oracle',
    'create_deutsch_circuit'
]