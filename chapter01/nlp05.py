# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = "I am an NLPer"
    word_list = s.split()
    word_bi_gram = zip(word_list[0:len(word_list)-1],word_list[1:])
    print(*word_bi_gram)

    char_list = list(s)
    char_bi_gram = [c1+c2 for c1,c2 in zip(char_list[0:len(char_list)-1],char_list[1:])]
    print(char_bi_gram)
