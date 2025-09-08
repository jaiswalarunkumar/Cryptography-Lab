import numpy as np

# Key matrix (must be square and invertible mod 26)
key = np.array([[3, 3],
                [2, 5]])

text = input("Enter a message: ").upper()

# Remove spaces and make length even
text = text.replace(" ", "")
if len(text) % 2 != 0:
    text += "X"

print("Plaintext:", text)

# Convert letters to numbers (A=0,...,Z=25)
nums = [ord(ch) - 65 for ch in text]

# Split into pairs
pairs = [nums[i:i+2] for i in range(0, len(nums), 2)]

cipher = ""

for pair in pairs:
    vec = np.array(pair)
    enc = key.dot(vec) % 26
    for val in enc:
        cipher += chr(val + 65)

print("Encrypted Text:", cipher)
