from base64 import b64decode, b64encode
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key(master_password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100_000
    )
    return kdf.derive(master_password.encode())


def encrypt(text: str, master_password: str):
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded = text + (16 - len(text) % 16) * chr(16 - len(text) % 16)
    ct = encryptor.update(padded.encode()) + encryptor.finalize()
    return b64encode(salt + iv + ct).decode()


def decrypt(ciphertext: str, master_password: str):
    data = b64decode(ciphertext)
    salt, iv, ct = data[:16], data[16:32], data[32:]
    key = derive_key(master_password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded = decryptor.update(ct) + decryptor.finalize()
    pad_len = padded[-1]
    return padded[:-pad_len].decode()


# Usage
master = "MyMasterPassword123!"
encrypted = encrypt("Hello", master)
print(f"Encrypted msg: {encrypted}")
print(f"Decrypted message: {decrypt(encrypted, master)}")
