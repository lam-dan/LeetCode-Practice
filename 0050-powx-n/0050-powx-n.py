class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 # Base Case: x^0 = 1

        # handle negative exponents by coverting to reciprocal
        if n < 0:
            x = 1.0/x
            n = -n
        
        result = 1 # Accumulator for the final answer

        # Iterative Binary Exponentiation
        while n != 0:
            if n % 2 == 1:
                result *= x # Multiply result when exponent is odd
                n -= 1
            x *= x # Square the base
            n //= 2 # Halve the exponent
        return result