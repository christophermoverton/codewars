import re 
import testcase_study21
def wrapper(f):
    def fun(l):
        # complete the function
        pat = r'\d{10}$'
        nl = []
        for i in l:
            ostr = re.search(pat, i).group(0)
            ostr = '+91 '+ ostr[0:5] + ' '+ostr[5:10]
            nl.append(ostr)
        return f(nl)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

    