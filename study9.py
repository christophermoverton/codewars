import testcase_study9
import re
pat = r"^[\+\-]?[0-9]*\.[0-9]*$"
pat2 =r"\d\.\d$"
N = int(input())
for i in range(N):
    fl = input()
    print(bool(re.match(pat,fl)))
    print(re.search(pat,fl))
    # print(re.findall(pat2,fl))