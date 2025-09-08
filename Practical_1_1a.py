import numpy as np

def matrix_operations():
    """
    Performs matrix addition, subtraction, and multiplication on two 3x3 matrices
    represented as nested lists.
    """
    print("--- Question 1: Matrix Operations ---")
    matA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    # Matrix Addition
    result_add = [[matA[i][j] + matB[i][j] for j in range(len(matA[0]))] for i in range(len(matA))]
    print(f"Matrix A + Matrix B = {result_add}")

    # Matrix Subtraction
    result_sub = [[matA[i][j] - matB[i][j] for j in range(len(matA[0]))] for i in range(len(matA))]
    print(f"Matrix A - Matrix B = {result_sub}")

    # Matrix Multiplication
    result_mul = np.dot(matA, matB)
    print(f"Matrix A * Matrix B = {result_mul.tolist()}")
    print("\n" + "-"*40 + "\n")