def minOperations(n):
    """
    Compute the minimum number of operations for the Copy All and Paste task.

    Args:
        n (int): Input value

    Returns:
        int: Minimum number of operations
    """
    if n < 2:
        return 0
    
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    return sum(factors)
