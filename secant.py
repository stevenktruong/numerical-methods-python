import math

def secant(f, init, eps, N=100):
    """
    Implementation of the secant method
    Parameters:
        f    - function to perform the secant method on
        df   - the derivative of f
        init - initialization for the secant method (list with 2 elements)
        eps  - short for epsilon, which is our tolerance level
        N    - how many iterations before we decide the sequence diverges
    """

    class ConvergenceError(Exception):
        pass

    p = init
    n = 1
    while n < 100:
        # Calculate p[n+1] from p[n] and p[n-1]
        p.append(
            p[n] - f(p[n])*(p[n]-p[n-1]) / (f(p[n])-f(p[n-1]))
        )

        # Check for convergence
        if abs(p[n] - p[n+1]) < eps:
            return p
        n = n + 1

    # p[100] doesn't exist
    if abs(p[n-1] - p[n-2]) >= eps:
        raise ConvergenceError("Sequence does not converge")

# f(x) = 3x - exp(x)
def f(x):
    return 3*x - math.exp(x)

# Start iteration
p = secant(f,[1,2],10**-5)
for i in range(0,len(p)):
    if p[i] > 0:
        print(f"{i}  {p[i]}")
    else:
        print(f"{i} {p[i]}")