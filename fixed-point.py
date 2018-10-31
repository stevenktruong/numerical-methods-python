import math

def fixed_point(f,init,N=100):
    """
    Implementation of the fixed-point method
    Parameters:
        f    - Function to use
        init - Initialization for the algoirthm
        N    - Number of iterations

    Return value:
        p - An array containing the iterations of the method
    """

    p = [init]
    for i in range(0,N):
        p.append(f(p[i]))

    return p

# f(x) = cos(x)
def f(x):
    return math.cos(x)

# Start iteration
p = fixed_point(f,1,4)
for i in range(0,len(p)):
    if p[i] > 0:
        print(f"{i}  {p[i]}")
    else:
        print(f"{i} {p[i]}")