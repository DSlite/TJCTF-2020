a = b'\x02\x19\x01\x16Q\r\x07\nS\x02)\x1a1=EE2\x0e=G/D\nRY)\nV\x1bJ'
key = "vsbb7"

string = ""
for i in range(len(a)):
    string += chr(a[i]^ord(key[i%5]))

print(string)
