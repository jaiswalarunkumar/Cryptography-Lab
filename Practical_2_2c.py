# Affine Cipher

message = input("Enter message: ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))

cipher = ""

for ch in message.upper():
    if ch.isalpha():
        cipher += chr(((a * (ord(ch) - 65) + b) % 26) + 65)
    else:
        cipher += ch

print("Encrypted:", cipher)