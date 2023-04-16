import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import PIL.Image as Image

class CBCDecryption:
    def __init__(self, key, iv):
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        self.decryptor = self.cipher.decryptor()

    def decrypt(self, ciphertext):
        return self.decryptor.update(ciphertext)

def DecryptImage(decryption, image, output):
    with open(image, 'rb') as reader:
        with open(output, 'wb') as writer:
            image_data = reader.read()
            header, body = image_data[:54], image_data[54:]
            body = decryption.decrypt(body)
            writer.write(header + body)
            writer.close()
            reader.close()

def main():
    key = b'JOINTSCTF2023'
    key = key.ljust(32, b'\x35')
    
    iv = key[:16]
    iv = bytearray(iv)
    for i in range(16):
        iv[i] = iv[i] ^ 0x35
    iv = bytes(iv)

    AesCbc = CBCDecryption(key, iv)
    DecryptImage(decryption=AesCbc, image='/Kompetisi/JCTF2023/crypto1/out.bmp', output='flag_decrypted.jpg')

if __name__ == '__main__':
    main()