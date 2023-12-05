import random
from hashlib import sha256

# secp256k1
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
a = 0
b = 7
Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

#
def generate_private_key():
    return random.randint(1, n - 1)


def generate_public_key(private_key):
    x, y = multiply((Gx, Gy), private_key)
    return (x, y)

def add(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    x1, y1 = p1
    x2, y2 = p2

    if p1 == p2:

        s = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:

        s = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return x3, y3


def multiply(point, scalar):
    result = None
    for bit in bin(scalar)[2:]:
        result = add(result, result)
        if bit == '1':
            result = add(result, point)
    return result


private_key = generate_private_key()
public_key = generate_public_key(private_key)


def encrypt(plaintext, public_key):

    ephemeral_private_key = generate_private_key()
    ephemeral_public_key = generate_public_key(ephemeral_private_key)


    shared_secret = multiply(public_key, ephemeral_private_key)[0]


    ciphertext = []
    for char in plaintext:
        shared_secret_hash = int.from_bytes(sha256(str(shared_secret).encode()).digest(), 'big')
        encrypted_char = ord(char) ^ shared_secret_hash
        ciphertext.append(encrypted_char)

    return ephemeral_public_key, ciphertext


def decrypt(ciphertext, ephemeral_public_key, private_key):

    shared_secret = multiply(ephemeral_public_key, private_key)[0]


    decrypted_text = ''
    for encrypted_char in ciphertext:
        shared_secret_hash = int.from_bytes(sha256(str(shared_secret).encode()).digest(), 'big')
        decrypted_char = chr(encrypted_char ^ shared_secret_hash)
        decrypted_text += decrypted_char

    return decrypted_text


plaintext = "Vladyslav Dryk"
print("Original:", plaintext)

public_key2, ciphertext = encrypt(plaintext, public_key)
print("Encrypted:", ciphertext)
for i in ciphertext:
    print(i)

decrypted_text = decrypt(ciphertext, public_key2, private_key)
print("Decrypted:", decrypted_text)
