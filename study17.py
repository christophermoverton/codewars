import math
import os
import random
import re
import sys
import datetime
import testcase_study17

# Complete the time_delta function below.
def time_delta(t1, t2):
    datetime_object_t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    datetime_object_t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    tdiff = datetime_object_t1-datetime_object_t2
    return str(int(round(abs(tdiff.total_seconds()))))



t = int(input())
ans = []
for t_itr in range(t):
    t1 = input()

    t2 = input()

    delta = time_delta(t1, t2)
    ans.append(delta)
    print(delta)

import testcase_study17_out

for i in range(t):
    tdiff = input()
    if ans[i]!=tdiff:
        print('tdiff:' + tdiff)
        print('ans: ' + ans[i])