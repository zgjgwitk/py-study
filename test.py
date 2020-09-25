# -*- coding: utf-8 -*-
#print('heehda')
s = "ABCD"
b = bytearray()
b.extend(map(ord, s))
for a in b:
    print(a)