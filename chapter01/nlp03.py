# -*- coding: utf-8 -*-

if __name__ == "__main__":
    pi_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    pi_list = [ len(p.replace(",", "").replace(".", "")) for p in pi_str.split()]
    print(pi_list)

