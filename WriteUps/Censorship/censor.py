from pwn import *
import re

r = remote("p1.tjctf.org", 8003)
line = r.recvline()
line = re.sub("[^0-9+]", "", line)
r.sendline(str(eval(line)))

r.interactive()