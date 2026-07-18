from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

sim = AerSimulator()

dynamic_probabilities = []

# 1. The Time Loop
for t in range(1, 6):
    # Create 3 new nodes/qubits for each spin state change
    qc = QuantumCircuit(3)
    
    for step in range(1):
        # Rotating qubits/nodes
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
    dynamic_probabilities.append(prob_000)
    print(f"Time Step {t} -> Probability of '000': {prob_000:.3f} | Total Counts: {counts}")



# Plotting the data
time_steps = [1, 2, 3, 4, 5]
 # The '000' state data

plt.plot(time_steps, dynamic_probabilities, marker='o', linestyle='-', color='b')
plt.title("Volume Fluctuation (The 'Breathing' Effect)")
plt.xlabel("Time Step (t)")
plt.ylabel("Probability of Base Volume State ('000')")
plt.grid(True)

plt.show()