import hashlib
import re

with open('Titanic.txt', 'r') as file:
    for line in file:
        for word in line.split():
            sword = "tjctf{" + re.sub('[^a-zA-Z0-9\'\".,/]', '', word).lower() + "}"
            md5 = hashlib.md5(sword).hexdigest()
            if md5 == "9326ea0931baf5786cde7f280f965ebb":
                print sword
