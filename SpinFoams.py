from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# We only need one simulator instance
sim = AerSimulator()

# 1. The Time Loop
for t in range(1, 6):
    # Create a FRESH universe at the start of each time step!
    qc = QuantumCircuit(3)
    
    # 2. Apply our time-steps 't' times
    for step in range(t):
        # First, rotate all qubits (Kinetic Step)
        for qubit in range(3):
            qc.rx(0.2, qubit)
            
        # Second, connect them
        qc.cz(0,1)
        qc.cz(1,2)
        qc.cz(2,0)
        
    for q in range(3):
        qc.h(q)
        
    qc.measure_all()
    
    # 4. Simulate this specific time step inside the loop
    job = sim.run(qc, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    # 5. Extract the probability of the '000' state
    prob_000 = counts.get('000', 0) / 1024
    
    print(f"Time Step {t} -> Probability of '000': {prob_000:.3f} | Total Counts: {counts}")