**A small qiskit qiskit 2.0 primitives project showcasing that space is merely an emergence of quantum relations
rather than a container as assumed in classical (Newtonian) physics.**

## SPIN NETWORK
This was achieved by entangling three qubits together using the cz gate (Controlled-Z gate), to set the qubits
into an entangled state with the results representing the "Area Operator" snapping to its lowest possible physical value:
one Planck area, which locks the qubits into a non-zero entangled state.
The Hadamard gate (qc.h) sets the qubits in superposition.
Remove the cz gates and you end up with an "area" of zero as space no longer exists.

## SPIN FOAMS
Remember the spin network (the "atom" of space) that I just explained above, Spin Foams is basically that but with the
introduction of time. You can Imagine the spin network we built as the static "atom" of space. We know that the
universe is in 4D rather than 3D so Spin Foams basically introduces the concept of time into the Spin Network to make
the 3D spatial geometry into a 4D spacetime history as described by General Relativity.
Now let's move away from the theoretical for now and focus on the code logic to understand how it simulates this phenomena.
the t represents the state of a space "atom" or spin network after each iteration from 1 through 5. The
for loop facilitates the creation of 3 qubits providing a blank quantum slate before any entanglement occurs.
For the first step, the qc.rx gate rotates the qubits (nodes/knots) causing a change in volume. The change in volume
is determined by taking the product of the base planck volume and multiplying it by a mathematical value derived
from the spin state.
From a theoretical standpoint the qc.rx gate represents kinetic energy.
After reaching maximum expansion at a threshold, the volume starts to contract back to zero.
This process repeats causing a sort of breathing effect that can also be observed after running the code.
This "breathing" effect along with the restructuring of the entanglement lines(cz gates) with respect to changes in volume in the node,
is what is known as the passage of time.
