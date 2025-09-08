def decrypt_caesar():

    plaintext = input("Enter the message to decrypt: ")


    while True:
        try:
            key = int(input("Enter the shift key (a number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the key.")

    ciphertext = ""
    for char in plaintext:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            ciphertext += shifted_char
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            ciphertext += shifted_char
        else:
            ciphertext += char

    print(f"Original message: {plaintext}")
    print(f"Decrypted message: {ciphertext}")

decrypt_caesar()