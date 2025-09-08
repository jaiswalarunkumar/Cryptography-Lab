message = input("Enter message: ")
key = int(input("Enter key: "))

cipher = ""

for ch in message.upper():
    if ch.isalpha():
        cipher += chr(((ord(ch) - 65) * key) % 26 + 65)
    else:
        cipher += ch

print("Decrypted:", cipher)
