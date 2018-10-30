import math

def steffensen(f,init,N=100):
    """
    Implementation of Steffensen's method
    Parameters:
        f    - Function to use
        init - Initialization for the algoirthm
        N    - Number of iterations

    Return value:
        p - An array containing the iterations of Steffensen's method
    """

    # Aitken's Delta^2 method
    def delta_squared(p):
        return p[0] - ((p[1]-p[0])**2) / (p[2]-2*p[1]+p[0])

    # p[i] gives you the values in the i-th step
    p = [[init]]

    for i in range(0,N):
        p[i].append( f(p[i][0]) ) # p_i^(1)
        p[i].append( f(p[i][1]) ) # p_i^(2)
        p.append([ delta_squared(p[i]) ]) # Initialization for next step

    return p

# f(x) = cos(x)
def f(x):
    return math.cos(x)

# Start iteration
p = steffensen(f,1,2)
for i in range(0,len(p)):
    for j in range(0,len(p[i])):
        if p[i][j] > 0:
            print(f"p_{i}^{j}  {p[i][j]}")
        else:
            print(f"p_{i}^{j} {p[i][j]}")