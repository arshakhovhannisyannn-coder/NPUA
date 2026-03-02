import numpy as np

x  = np.random.randint(0, 10, size=(2, 3))
x2 = np.random.randint(0, 10, size=(2, 3))

print("x =\n", x)
print("x2 =\n", x2)


W1 = np.random.random((3, 3)) - 0.5   # (3x3)
b1 = np.random.random((1, 3)) - 0.5   # (1x3) 
Z1  = x @ W1 + b1    
A1  = np.maximum(0, Z1)  
print("Z1 =\n",Z1)
print("A1 =\n", A1)


W2 = np.random.random((3, 3)) - 0.5   # (3x3)
b2 = np.random.random((1, 3)) - 0.5   # (1x3) 
Z2  = A1 @ W2 + b2   
A2  = np.maximum(0, Z2)  
print("Z2 =\n",Z2)
print("A2 =\n", A2)



W3 = np.random.random((3, 1)) - 0.5  
b3 = np.random.random((1, 1)) - 0.5   
Z3  = A2 @ W3 + b3    
A3  = 1 / (1 + np.exp(-Z3)) 
print("Z3 =\n",Z3)