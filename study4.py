
import math
import os
import random
import re
import sys
import testcase_study4
from collections import OrderedDict


if __name__ == '__main__':
    s = input()
    d = OrderedDict()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    d = {k: v for k, v in sorted(d.items(), key=lambda item: (-item[1],item[0]))}
    for i, el in enumerate(d):
        if i > 2:
            break
        print(el +" "+str(d[el]))