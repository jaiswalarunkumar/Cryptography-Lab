def second_largest_sum_tuple():
    print("--- Question 2: Second Largest Sum Tuple ---")
    nested_tuples = ((1, 5, 2), (8, 2, 3), (4, 9, 1), (7, 6, 5))
    sums = [(sum(t), t) for t in nested_tuples]
    sums.sort(key=lambda x: x[0], reverse=True)

    if len(sums) > 1:
        print(f"The nested tuples are: {nested_tuples}")
        print(f"The tuple with the second largest sum is: {sums[1][1]}")
    else:
        print("There are not enough tuples to find the second largest sum.")
    print("\n" + "-"*40 + "\n")