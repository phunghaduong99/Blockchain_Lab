from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
n = 50
 
# Initialization
X = np.random.randint(
          -100, 100, 
          (n, 50),
          )
fBar = []
# Clone an array
def Cloning(array): 
    array_copy = [] 
    array_copy.extend(array) 
    return array_copy

def fx_i(elem):
    elem_2 = np.multiply(elem, elem)
    return np.sum(elem_2)

for y in range (0, 900):
  X = sorted(X, key=fx_i)
  # Evaluate
  fx = np.sum(
      np.multiply(X, X), 
      axis=1
      )
  
  # Selection
  fBar.append(fx[0])

  for x in range (int(n*80/100), n):
        X[x] = Cloning(X[np.random.randint(0, n*20/100)])

  # Crossover
  for i in range(0, int(n*50/100)):
    father = np.random.randint(int(n*10/100), n)
    mother = np.random.randint(int(n*10/100), n)
    for j in range (0, len(X[father])):
      if np.random.rand() < 0.5:
        temp = X[father][j]
        X[father][j] = X[mother][j]
        X[mother][j] = temp

  # Mutation
  index = np.random.randint(0, n*10/100)
  bit = np.random.randint(0, len(X[0]))
  mutation = abs(Cloning(X[int(index)])[int(bit)] )
  X[1][int(bit)] = np.random.randint(mutation*(-1) , mutation +1  )

plt.plot(fBar)
plt.ylabel('fx')
plt.show()
print(fBar)







