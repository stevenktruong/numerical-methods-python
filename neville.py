from math import exp

def neville(x, nodes):
    """
    Implementation of Neville's method
    Parameters:
    x     - point to estimate f at
    nodes - list containing known points on f(x)

    Output:
    List of lists containing the iterations
    The (only) element of the last list contains the final approximation
    For the rest, p[i][j] = f[xj,...,xj+i]
    For example,
        p[0][0] = f[x0]
        p[1][2] = f[x2,x3]
        p[2][3] = f[x3,x4,x6]
        etc.
    """
    p = [ [y for (x, y) in nodes] ]
    i = 1 # len(nodes)-i gives us the number of elements in the last array of p
    while len(nodes)-i > 0:
        iteration = []
        for j in range(0,len(nodes)-i):
            iteration.append( ((x-nodes[j][0])*p[-1][j+1] - (x-nodes[j+i][0])*p[-1][j]) / (nodes[j+i][0]-nodes[j][0]) )
        p.append(iteration)
        i = i + 1

    return p

nodes = [(1,0.75), (1.3,0.63), (1.5,0.55), (2,0.49)]
p = neville(1.6,nodes)

# p[i][0] = f[x0,...,xi]
# p[i][1] = f[x1,...,xi+1]
# etc.