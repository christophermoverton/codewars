import testcase_study18

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream):
    for _ in range(n):
        a = stream.get_next()
        print(a)
        ans.append(a)


queries = int(input())
ans = []
sub_queries = []
sub_ans = []
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if len(ans)< 31:
        sub_queries.append([stream_name,n])
        sub_ans = ans[0:]
    if stream_name == "even":
        print_from_stream(n, EvenStream())
    else:
        print_from_stream(n, OddStream())

import testcase_study18_out
for i,aval in enumerate(ans):
    val = input()
    if str(aval) != val:
        print('answer: '+str(aval))
        print('expected: '+val)
        print('i: '+str(i))         
