import hashlib

with open('Dictionary.txt', 'r') as f:

    for line in f:
        line = line.strip()

        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        expected = "9be9f4182c157b8d77f97d3b20f68ed6b8533175831837c761e759c44f6feeb8"

        if sha256_hash == expected:
            print(f"{line} : {sha256_hash}")