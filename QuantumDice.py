from pyquil import Program, get_qc
from pyquil.gates import H

def throw_octahedral_die():
  
  qvm = get_qc("3q-qvm") #logb2(8) = 3
  prog = Program() # create program
  ro = prog.declare("ro", "BIT", 3) #declare output memory space
  
  for q in range(3):
    prog += H(q) #apply Hadamard gate to each qubit to create equal probability
  for q in range(3):
    prog.measure(q, ro[q]) #check if the cät is dead
  
  result = qvm.run(qvm.compile(prog))[0]
  temp = 0
  for q in result: #bin to dec
    temp = 2*temp + q
  
  return temp + 1 #shift 0 -> 1

def throw_polyhedral_die(n): #extend to any-sided die
  
  qubits = int(math.ceil(math.log(n, 2)) #get number of qubits needed
  qvm = get_qc(f"{qubits}q-qvm")
  prog = Program() 
  ro = prog.declare("ro", "BIT", qubits)
  
  for q in range(qubits):
    prog += H(q)
  for q in range(qubits):
    prog.measure(q, ro[q])
  
  result = qvm.run(qvm.compile(prog))[0]
  temp = 0
  for q in result:
    temp = 2*temp + q
  
  return int(math.floor(temp*(n/2**qubits))+1) #a bit of an unfair scaling down
