# -*- coding: utf-8 -*-

from nlp05 import char_n_gram

if __name__ == "__main__":
    setX = set(char_n_gram("paraparaparadise",2))
    setY = set(char_n_gram("paragraph",2))
    print("X", setX)
    print("Y", setY)
    print("和集合", setX | setY)
    print("積集合", setX & setY)
    print("差集合(X-Y)", setX - setY)
    print("差集合(Y-X)", setY - setX)
    print("集合Xにseが含まれるか？", "se" in setX)
    print("集合Yにseが含まれるか？", "se" in setY)

