f = open('hex.txt', 'r')
text = f.read()
word = ""
for w in text.split():
    n = int(w, 16)
    n = n ^ 0x91 # 1001 0001
    word += chr(n)

print word
