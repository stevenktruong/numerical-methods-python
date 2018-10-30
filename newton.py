def newton(f, df, init, eps, N=100):
    """
    Implementation of Newton's method
    Parameters:
        f    - function to perform Newton's method on
        df   - the derivative of f
        init - initialization for Newton's method
        eps  - short for epsilon, which is our tolerance level
        N    - how many iterations before we decide the sequence diverges
    """

    class ConvergenceError(Exception):
        pass

    # Newton's method is a special case of the fixed-point method for the following function
    def g(x):
        return x - f(x)/df(x)

    p = [init]
    n = 0
    while n < 100:
        # Calculate p[n+1]
        p.append(g(p[n]))

        # Check for convergence
        if abs(p[n] - p[n+1]) < eps:
            return p
        n = n + 1

    # p[100] doesn't exist
    if abs(p[n-1] - p[n-2]) >= eps:
        raise ConvergenceError("Sequence does not converge")

# f(x) = x^2 - 4x + 3
def f(x):
    return x**2 - 4*x + 3

# f'(x) = 2x - 4
def df(x):
    return 2*x - 4

# Start Newton's method
p = newton(f,df,1.99,10**-5)
for i in range(0,len(p)):
    if p[i] > 0:
        print(f"{i}  {p[i]}")
    else:
        print(f"{i} {p[i]}")
