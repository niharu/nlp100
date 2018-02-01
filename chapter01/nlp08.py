# -*- coding: utf-8 -*-

def cipher(word):
    return [str(219 - ord(s)) if s.islower() else s for s in list(word)]

def decipher(cipher_list):
    return [chr(219 - int(s)) if s.isnumeric() else s for s in cipher_list]

if __name__ == "__main__":
    s = "abcDefgあいう"
    print(cipher(s))
    print(decipher(cipher(s)))
