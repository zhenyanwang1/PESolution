from string import ascii_lowercase
from itertools import cycle
print(ascii_lowercase)
def gen_keys():
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                yield ord(a),ord(b),ord(c)
content=[int(char) for char in open("cipher.txt").read().split(",")]
for key in gen_keys():
    s="".join([chr(char ^ key_char) for char,key_char in zip(iter(content),cycle(key))])
    if all([x in s for x in ['the',' a ']]):
        print(sum([ord(char) for char in s]))