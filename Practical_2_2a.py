def encrypt_caesar():
    """Encrypts a message using the Caesar cipher with user input."""
    # Get the plaintext message from the user
    plaintext = input("Enter the message to encrypt: ")

    # Get the key (shift value) from the user
    # We use a while loop to ensure the input is a valid number
    while True:
        try:
            key = int(input("Enter the shift key (a number): "))
            break  # Exit the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a number for the key.")

    ciphertext = ""
    for char in plaintext:
        if 'a' <= char <= 'z':
            # For lowercase letters
            shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            ciphertext += shifted_char
        elif 'A' <= char <= 'Z':
            # For uppercase letters
            shifted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            ciphertext += shifted_char
        else:
            # For non-alphabetic characters (spaces, symbols, etc.)
            ciphertext += char

    print(f"Original message: {plaintext}")
    print(f"Encrypted message: {ciphertext}")

# Run the encryption function
encrypt_caesar()