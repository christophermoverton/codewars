import re
import testcase_study11

pat = r'[A-Z]{1}'
pat2 = r'\d'
pat3 = r'^[A-Za-z0-9]{10}$'
check_patterns = {pat:2,pat2:3,pat3:None}
ans = {}
N = int(input())
for i in range(N):
    s = input()
    patt_pass = False
    for j,check_pattern in enumerate(check_patterns):
        # if i == 7:
        #     print(s)
        #     print(check_pattern)
        if j == 1 or j==0:
            res = re.findall(check_pattern,s)
            if len(res)<check_patterns[check_pattern]:
                print('Invalid')
                ans[i] = {'ans':'Invalid','s':s}
                patt_pass = False
                break
            else:
                patt_pass = True
        else:
            if not bool(re.search(check_pattern,s)):
                print('Invalid')
                ans[i]={'ans':'Invalid','s':s}
                patt_pass = False
                break
            else:
                patt_pass = True

    if patt_pass:
        k = list(set([i for i in s]))
        if len(k)!= len(s):
            print('Invalid')
            ans[i] = {'ans':'Invalid','s':s}
        else:
            print('Valid')
            ans[i]={'ans':'Valid','s':s}

import testcase_study11_out
for i in range(N):
    if ans[i]['ans'] != input():
        print(ans[i]['s'])
        print(ans[i]['ans'])
        print(i)

import testcase_study11_out