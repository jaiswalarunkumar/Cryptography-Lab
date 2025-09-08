def inverse(a, b):
    l1 = 0
    l2 = 1
    mod = b
    A = a
    B = b

    while (B > 0):
        q = A // B
        r = A % B
        A, B = B, r
        t = l1 - q * l2
        l1, l2 = l2, t

    # GCD check
    if (A != 1):
        return -1
    else:
        return l1 % mod   # normalize result


a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

inv = inverse(a, b)

if (inv == -1):
    print("The given value for the number can’t be found as inverse.")
else:
    print("The given inverse of number is:", inv)
