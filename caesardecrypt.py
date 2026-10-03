import string

alphabet = string.ascii_uppercase

ciphertext = input("> ").upper()

for i in range(1, 25):
    decypher_attempt = []
    for char in ciphertext:
        if char in alphabet:
            counter = 0
            for letter in alphabet:
                counter += 1
                if letter == char:
                    decypher_attempt.append(alphabet[(counter - i) % 26])
        else:
            decypher_attempt.append(char)
            
    print("".join(decypher_attempt))
