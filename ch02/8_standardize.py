import numpy as np

a= [173,181,168,175,179]
b= [1.73,1.81,1.68,1.75,1.79]

def standerdize(x):
    return (x -np.mean(x)/np.std(x))

print(standerdize(a))
print(standerdize(b))
