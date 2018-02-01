# -*- coding: utf-8 -*-

def n_gram(nlist, n):
    n_gram_list = []
    n_gram_list.append(nlist[0:len(nlist)-(n-1)])
    n_gram_list.extend([nlist[i:] for i in range(1,n)])
    return zip(*n_gram_list)

def n_gram_word(sentence, n):
    return n_gram(sentence.split(), n)

def n_gram_char(sentence, n):
    return n_gram(list(sentence), n)

if __name__ == "__main__":
    s = "I am an NLPer"
    print(*n_gram_word(s, 2))
    print(*n_gram_char(s, 2))

