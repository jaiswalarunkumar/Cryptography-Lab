def gf2_mul_mod(a: int, b: int, mod: int, p: int) -> int:
   
    result = 0
    while b:
        if b & 1:          
            result ^= a     
        b >>= 1            
        carry = a & (1 << (p - 1))  
        a <<= 1
        if carry:          
            a ^= mod
    return result


if __name__ == "__main__":
    mod = 0x11b
    p = 8

    a = 0x57
    b = 0x83
    res = gf2_mul_mod(a, b, mod, p)
    print(f"AES Example: (0x{a:02x} * 0x{b:02x}) mod 0x{mod:x} = 0x{res:02x}")
    mod4 = 0b10011
    p4 = 4
    a = 0b1011  # x^3 + x + 1
    b = 0b101   # x^2 + 1
    res2 = gf2_mul_mod(a, b, mod4, p4)
    print(f"GF(2^4) Example: result = {bin(res2)}")
