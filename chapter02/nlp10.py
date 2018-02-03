# -*- coding: utf-8 -*-

if __name__ == "__main__":
    wc = 0
    for line in open("hightemp.txt", "r"):
        wc += 1

    print(wc)
