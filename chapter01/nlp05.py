# -*- coding: utf-8 -*-

def _n_gram(target, n):
    return [target[i:i+n] for i in range(0, len(target) - (n -1))]

def word_n_gram(target, n):
    return [" ".join(s) for s in _n_gram(target.split(), n)]

def char_n_gram(target, n):
    return ["".join(s) for s in _n_gram(list(target), n)]

if __name__ == "__main__":
    s = "I am an NLPer"
    print("単語bi-gram",word_n_gram(s, 2))
    print("文字bi-gram",char_n_gram(s, 2))

