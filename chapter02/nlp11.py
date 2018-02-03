# -*- coding: utf-8 -*-

if __name__ == "__main__":
    f = open("_hightemp.txt", "w")
    for line in open("hightemp.txt", "r"):
        f.write(str(line).replace("\t", " "))
