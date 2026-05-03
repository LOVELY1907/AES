from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_msg = pad(message)
    ciphertext = cipher.encrypt(padded_msg.encode())
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    decrypted = cipher.decrypt(decoded).decode().strip()
    return decrypted

key = get_random_bytes(16)

message = input("Enter message: ")

encrypted = encrypt(message, key)
print("\nEncrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)