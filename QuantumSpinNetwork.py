from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3, 3)
#qc.measure_all()
for i in range(3):
    qc.h(i)

#qc.cz(0,1)
#qc.cz(1,2)
#qc.cz(2,0)

for i in range(3):
    qc.h(i)

qc.measure_all()

sim = AerSimulator()
job = sim.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print(counts)