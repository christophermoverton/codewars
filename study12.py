import testcase_study12_out

def print_formatted(number):
    # your code goes here
    bmax = "{0:b}".format(int(number))
    width = len(bmax)
    ostr=""
    for i in range(1,number+1):
        num = str(i).rjust(width," ")
        octn = "{0:o}".format(i).rjust(width," ")
        hexn = "{0:x}".format(i).rjust(width," ")
        binn = "{0:b}".format(i).rjust(width," ")
        if i == number:
            ostr+=num+" "+octn+" "+hexn+" "+binn
        else:
            ostr+=num+" "+octn+" "+hexn+" "+binn+"\n"
    print(ostr)
    return ostr
        


n = 17
ostr = print_formatted(n)
costr=""
for i in range(n):
    costr += input()+"\n"
print(costr)
for i,ch in enumerate(costr):
    if ch != ostr[i]:
        print(i)
        print(ch)
        break