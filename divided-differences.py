from math import exp

def divided_diff(nodes):
    """
    Implementation of divided differences
    Parameters:
    nodes - list containing known points on f(x)

    Output:
    A list of lists, where the first element of the i-th list gives the coefficient f[x1,x2,...,xi]
    """
    p = [ [y for (x, y) in nodes] ]
    i = 1 # len(nodes)-i gives us the number of elements in the last array of p
    while len(nodes)-i > 0:
        iteration = []
        for j in range(0,len(nodes)-i):
            iteration.append( (p[-1][j+1] - p[-1][j]) / (nodes[j+i][0]-nodes[j][0]) )
        p.append(iteration)
        i = i + 1

    return p

h = 0.1
s = 0.5
nodes = [(i/10, exp(i/10)) for i in range(0,5)]
p = divided_diff(nodes)

print("Coefficients")
for i in range(0,len(p)):
    x = f"f[{nodes[0][0]}"
    for j in range(1,i+1):
        x = x + f", {nodes[j][0]}"
    x = x + f"] = {p[i][0]}"
    print(x)

print("\nNewton's Forward Method")

# Using the coefficients for the Newton forward method
num = 0
for i in range(0,len(p)):
    n = p[i][0]
    for j in range(0,i):
        n = n * (s-j) * h
    num = num + n
    print(f"P{i} = {num}")