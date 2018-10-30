import math
import numpy as np
import matplotlib.pyplot as plt

def lagrange_polynomial(nodes,f):
    """
    Calculates the Lagrange polynomial through the given nodes
    Parameters:
        nodes - Points to define the Lagrange polynomial with
        f     - The function to create the polynomial for

    Returns value:
        P - The Lagrange polynomial
    """

    y = f(nodes)
    def P(x):
        output = 0
        for i in range(0,len(nodes)):
            # Calculate the polynomial that goes through (node[i],y[i]) and 0 through the other nodes
            poly = y[i]
            for j in range(0,len(nodes)):
                if j == i:
                    continue
                poly *= (x-nodes[j]) / (nodes[i]-nodes[j])
            output += poly
        return output

    return P

# Runge's function, 1/(x^2+1)
def f(x):
    return 1 / (x**2 + 1)

# nodes = np.arange(start=-5,stop=6,step=1)
nodes = np.array( [5*math.cos(k*math.pi/10) for k in range(0,11)] )

P = lagrange_polynomial(nodes,f)

x = np.linspace(-5,5,num=100)
fx = f(x)
Px = P(x)

fig, ax = plt.subplots()
ax.set_xlim(left=-5,right=5)
ax.set_ylim(bottom=0,top=1.5)

ax.plot(x,fx)
ax.plot(x,Px)
plt.show()