## Cryptography - Easy CBC

In this challenge, we were given an image that has been encrypted.

![res](assets/out.bmp)

This image has been encrypted with the following [Python script](assets/challenge.py) that implemented AES-CBC encryption.

> AES-CBC (Advanced Encryption Standard - Cipher Block Chaining) is a method of encrypting data to keep it secure. It works by dividing the data into blocks, and then encrypting each block with a secret key using the AES algorithm. The blocks are linked together in a chain, with each block XORed with the previous block before being encrypted. This helps to make it harder for patterns in the plaintext to be seen in the ciphertext.

The code snippet below.

```python
# !pip install certifi==2021.10.8
# !pip install cffi==1.15.0
# !pip install cryptography==36.0.2
# !pip install Pillow==9.0.1
# !pip install wincertstore==0.2
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import PIL.Image as Image

class CBCEncryption:
    def __init__(self, key, iv):
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        self.encryptor = self.cipher.encryptor()

    def encrypt(self, image):
        return self.encryptor.update(image)

    def finalize_encrypt(self):
        return self.encryptor.finalize()

def EncryptImage(encryption, image, output):
    output = output + '.bmp'
    image = Image.open(image)
    image.save('temp.bmp')
    with open('temp.bmp', 'rb') as reader:
        with open(output, 'wb') as writer:
            image_data = reader.read()
            header, body = image_data[:54], image_data[54:]
            body += b'\x35' * (16 -(len(body) % 16))
            body = encryption.encrypt(body) + encryption.finalize_encrypt()
            writer.write(header + body)
            writer.close()
            reader.close()
    os.remove('temp.bmp')

def main():
    key = b'JOINTSCTF2023'
    key = key.ljust(32, b'\x35')
    
    iv = key[:16]
    iv = bytearray(iv)
    for i in range(16):
        iv[i] = iv[i] ^ 0x35
    iv = bytes(iv)

    AesCbc = CBCEncryption(key, iv)
    EncryptImage(encryption=AesCbc, image='flag.jpg', output='out')

if __name__ == '__main__':
    main()
```

It defines a class called `CBCEncryption` to handle encryption using the provided `key` and initialization `vector (IV)`, and a function called `EncryptImage` to encrypt the image file. The `key` and `iv` values are manipulated to ensure they are of the correct length. The main function initializes the encryption class with a `key` and `IV`, and then calls the `EncryptImage` function to encrypt an image file called "flag.jpg" and save the output as "out.bmp".

The `EncryptImage` function opens the input image file and saves a temporary copy of it as a BMP file. It then reads the image data from the temporary file, splits the data into a header section and a body section, and pads the body section with additional data to make it a multiple of 16 bytes long. It then uses the provided `CBCEncryption` object to encrypt the padded body section, and saves the encrypted data along with the original header section as the output BMP file.

To decrypt the image, we should do the reverse engineering using the same `key` and `IV` that were used to encrypt the data, and perform the decryption process in the reverse order of the encryption process. Beside that, it also important to unpad the decrypted data to remove any additional bytes that were added during the padding process. The decryptor script can be seen in [here](decrypt.py).

The code snippet below.

```python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import PIL.Image as Image

# define a class for CBC decryption
class CBCDecryption:
    # initialization function to set up the cipher and decryptor
    def __init__(self, key, iv):
        self.cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        self.decryptor = self.cipher.decryptor()

    # function to decrypt ciphertext
    def decrypt(self, ciphertext):
        return self.decryptor.update(ciphertext)

# function to decrypt an image using a CBC decryption object
def DecryptImage(decryption, image, output):
    # open the input image file and create the output file
    with open(image, 'rb') as reader:
        with open(output, 'wb') as writer:
            # read the image data and separate the header and body
            image_data = reader.read()
            header, body = image_data[:54], image_data[54:]
            # decrypt the body of the image
            body = decryption.decrypt(body)
            # write the decrypted image data to the output file
            writer.write(header + body)
            writer.close()
            reader.close()

# main function to set up decryption object and decrypt image
def main():
    # set up the key and IV for decryption
    key = b'JOINTSCTF2023'
    key = key.ljust(32, b'\x35')
    iv = key[:16]
    iv = bytearray(iv)
    for i in range(16):
        iv[i] = iv[i] ^ 0x35
    iv = bytes(iv)

    # create a CBC decryption object with the key and IV
    AesCbc = CBCDecryption(key, iv)
    # decrypt the image using the decryption object
    DecryptImage(decryption=AesCbc, image='out.bmp', output='flag_decrypted.jpg')

if __name__ == '__main__':
    main()
```

Run it, and we got the flag. 

![res](flag_decrypted.jpg)

</br>

So, this is the flag.

```
JCTF2023{n4rim0_in9_pAndum}
```
