# -*- coding: utf-8 -*-
import random

def typoglycemia(sentence):
    word_list = sentence.split()
    typoglycemia_list = []
    for word in word_list:
        if len(word) > 3:
            typo_word = list(word[1:len(word)-1])
            random.shuffle(typo_word)
            #print(word[0], "".join(typo_word), word[-1])
            typoglycemia_list.append(str(word[0] + "".join(typo_word) + word[-1]))
        else:
            typoglycemia_list.append(word)

    return " ".join(typoglycemia_list)

if __name__ == "__main__":
    #s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    s = """こんにちは　みなさん　おげんきですか？　わたしは　げんきです"""
    print(typoglycemia(s))
