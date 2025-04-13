# Recursively calculates the factorial of a non-negative integer n.
# Returns 1 if n is 0 (base case), otherwise returns n multiplied by the factorial of (n - 1).
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
