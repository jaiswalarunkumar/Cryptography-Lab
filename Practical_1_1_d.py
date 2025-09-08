def dictionary_operations():
   
    print("--- Question 4: Dictionary Operations ---")
    my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

    # Accessing an element
    print(f"Accessing 'apple': {my_dict['apple']}")

    # Adding a new key-value pair
    my_dict['date'] = 4
    print(f"After adding 'date': {my_dict}")

    # Modifying a value
    my_dict['banana'] = 20
    print(f"After modifying 'banana': {my_dict}")

    # Deleting an element
    del my_dict['cherry']
    print(f"After deleting 'cherry': {my_dict}")

    # Getting all keys, values, and items
    print(f"Keys: {list(my_dict.keys())}")
    print(f"Values: {list(my_dict.values())}")
    print(f"Items: {list(my_dict.items())}")
    print("\n" + "-"*40 + "\n")
