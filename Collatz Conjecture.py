import matplotlib.pyplot as plt
import numpy as np

x=7
y=0

number=np.array([])
step=np.array([])


while x > 1:
    y+=1
    np.append(step, y)
    if x%2==0:
        x=x/2
        print(x)
    else:
        x=3*x+1
        print(x)
    np.append(number, x)

print("It took",y,"steps")
pritn(number)
plt.plot(step, number)
plt.show