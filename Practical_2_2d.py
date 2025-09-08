key = [[ 'A','B','C','D','E'],
       [ 'F','G','H','I','K'],
       [ 'L','M','N','O','P'],
       [ 'Q','R','S','T','U'],
       [ 'V','W','X','Y','Z']]

text = input("Enter a string that needs to be encrypted : ").upper()

pairs = []      # List for the encryption pairs
i = 0

while (i < len(text)):
    a = text[i]
    if (i+1 < len(text)):
        b = text[i+1]
        if (a == b):
            pairs.append([a,'X'])
            i += 1
        else:
            pairs.append([a,b])
            i += 2
    else:
        pairs.append([a,'X'])
        i += 1

print("Pairs :", pairs)

# Function to find position of a letter in key matrix
def find_position(ch):
    for r in range(5):
        for c in range(5):
            if key[r][c] == ch:
                return r, c

# Encryption
cipher_text = ""
for a, b in pairs:
    r1, c1 = find_position(a)
    r2, c2 = find_position(b)

    if r1 == r2:   # Same row
        cipher_text += key[r1][(c1+1)%5] + key[r2][(c2+1)%5]
    elif c1 == c2: # Same column
        cipher_text += key[(r1+1)%5][c1] + key[(r2+1)%5][c2]
    else:          # Rectangle rule
        cipher_text += key[r1][c2] + key[r2][c1]

print("Encrypted Text :", cipher_text)
