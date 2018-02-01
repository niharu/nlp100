# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = "paraparaparadise"
    s2 = "paragraph"
    clist1 = list(s1)
    clist2 = list(s2)
    setX = set([ c1+c2 for c1,c2 in zip(clist1[0:len(clist1)-1], clist1[1:])])
    setY = set([ c1+c2 for c1,c2 in zip(clist2[0:len(clist2)-1], clist2[1:])])
    print("X", sorted(setX))
    print("Y", sorted(setY))
    print("和集合", setX | setY)
    print("積集合", setX & setY)
    print("差集合(X-Y)", setX - setY)
    print("差集合(Y-X)", setY - setX)
    print("集合Xにseが含まれるか？", "se" in setX)
    print("集合Yにseが含まれるか？", "se" in setY)

