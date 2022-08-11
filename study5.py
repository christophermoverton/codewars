import testcase_study5
def solve(s):
    m = s.split()
    ws = []
    count = 0
    last = None
    for ch in s:
        if ch ==" ":
            if last != " ":
                last = ch
            count+=1
        else:
            if last == " ":
                ws.append(count)
                count = 0
                last = ch     
    print(ws) 
    k = []
    for i in m:
        nm = ""
        if len(i) == 1:
            nm = i.upper()
        else:
            nm = i[0].upper()+i[1:]
        k.append(nm)
    otstr = ""
    for i,el in enumerate(k):
        if i != len(k)-1:
            otstr+=el+" "*ws[i]
        else:
            otstr+=el
    return otstr

if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result + '\n')

