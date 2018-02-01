# -*- coding: utf-8 -*-

if __name__ == "__main__":
    ele_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    single_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    dict = {i+1:s[0] if i+1 in single_list else s[:2] for i,s in enumerate(ele_str.split())}
    print(dict)

