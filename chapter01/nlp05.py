# -*- coding: utf-8 -*-

def n_gram(nlist, n):
    return [nlist[i:i+n] for i in range(0, len(nlist) - (n -1))]

if __name__ == "__main__":
    s = "I am an NLPer"
    print("単語bi-gram",n_gram(s.split(), 2))
    print("文字bi-gram",n_gram(list(s), 2))
