def extended_gcd_iterative_simplified(a, b):
    # s1 and t1 are coefficients for a.
    # s2 and t2 are coefficients for b.
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    # Loop continues as long as b is greater than 0
    while b > 0:
        # Calculate quotient and remainder
        q = a // b
        r = a % b

        # Update a and b with the new values
        a = b
        b = r

        # Update the coefficients for a
        s = s1 - q * s2
        s1 = s2
        s2 = s

        # Update the coefficients for b
        t = t1 - q * t2
        t1 = t2
        t2 = t

    # When the loop ends, a is the GCD.
    # We return only the GCD value.
    return a

# Example usage:
num1 = 48
num2 = 18

gcd_val = extended_gcd_iterative_simplified(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_val}")