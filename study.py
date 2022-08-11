import re

def fun(s):
    regex = r'\b[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'
    if(re.fullmatch(regex, s)):
        return True
    else:
        return False

print(fun('iu89_in.plus@google.com'))
print(fun('ill@google.com'))

list = ['its@gmail.com1','mike13445@yahoomail9.server','rase23@ha_ch.com','daniyal@gmail.coma','thatisit@thatisit']
for i in list:
    print(fun(i))