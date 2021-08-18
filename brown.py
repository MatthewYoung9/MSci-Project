
import numpy as np
import random
import statistics
import matplotlib.pyplot as plt


epsilon = 2**(-10)
x_0 = 0
y_0 = 0




T = np.zeros(1000)

for i in range(1000):
    t=0
    x = 0
    y = 0  
    while x**2 + y**2 <1:
        x += random.choice([epsilon, -epsilon])
        y += random.choice([epsilon, -epsilon])
        t+= 1
    T[i]= t
    
print(T)
#plt.hist(T, bins = 400)
plt.hist([np.log(i) for i in T], bins = 40)
plt.show()








