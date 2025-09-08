def gcd(a, b):
    # Loop continues as long as b is greater than 0
    while b > 0:

        q = a // b  # Using integer division
        r = a % b

        # The new 'a' becomes the old 'b'
        a = b
        # The new 'b' becomes the remainder 'r'
        b = r

    # When the loop ends, 'a' holds the GCD
    return a

# Example usage:
num1 = 45
num2 = 18

result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")