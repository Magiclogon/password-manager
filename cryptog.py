from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from Crypto.Protocol.KDF import PBKDF2
import os


# Generating key for passwords database
salt = b'\xb4Keb\x97g`\x1bO9\x84\xc5Z\xef0\xca$C\x11\x97\xc8\xc5\xb5"\xd2v\x8d\xea\xf8\xceY\x82'
password = "mypassword"
key = PBKDF2(password, salt, dkLen=32)


# Encrypting password
def encrypt_password(passwd):
    iv = os.urandom(16)

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(passwd.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_password = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_password, iv


# Decrypting password
def decrypt_password(encrypted_password, iv):

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_password) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data.decode()

