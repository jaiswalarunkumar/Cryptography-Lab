def gf2_poly_add(poly1: list[int], poly2: list[int]) -> list[int]:
  
    max_len = max(len(poly1), len(poly2))

    p1 = [0] * (max_len - len(poly1)) + poly1
    p2 = [0] * (max_len - len(poly2)) + poly2

    result = [p1[i] ^ p2[i] for i in range(max_len)]  
    try:
        first_one = next(i for i, x in enumerate(result) if x == 1)
        return result[first_one:]
    except StopIteration:
        return [0]

poly_a = [1, 0, 0, 1, 1]
poly_b = [0, 1, 1, 0, 1]
result_poly = gf2_poly_add(poly_a, poly_b)

print(f"Polynomial 1 (coefficients): {poly_a}")
print(f"Polynomial 2 (coefficients): {poly_b}")
print(f"\nResulting polynomial (coefficients): {result_poly}")
