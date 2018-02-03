# -*- coding: utf-8 -*-

def n_gram(nlist, n):
    n_gram_list = []
    n_gram_list.append(nlist[0:len(nlist)-(n-1)])
    n_gram_list.extend([nlist[i:] for i in range(1,n)])
    return list(zip(*n_gram_list))

if __name__ == "__main__":
    s = "I am an NLPer"
    print("単語bi-gram",n_gram(s.split(), 2))
    print("文字bi-gram",n_gram(list(s), 2))

