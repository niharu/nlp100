# -*- coding: utf-8 -*-

def n_gram(nlist, n):
    n_gram_list = []
    n_gram_list.append(nlist[0:len(nlist)-(n-1)])
    n_gram_list.extend([nlist[i:] for i in range(1,n)])
    return zip(*n_gram_list)

if __name__ == "__main__":
    s = "I am an NLPer"
    print(*n_gram(s.split(), 2)) # 単語bi-gram
    print(*n_gram(list(s), 2)) # 文字bi-gram

