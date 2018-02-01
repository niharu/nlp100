# -*- coding: utf-8 -*-
from string import Template

if __name__ == "__main__":
    t = Template("${x}時の${y}は${z}")
    print(t.substitute(x=12,y="気温",z=22.4))
