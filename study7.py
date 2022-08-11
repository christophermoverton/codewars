import re

regex_integer_in_range = r"^[1-9]{1}\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.
#alternatimg digits

S = 'vineetdoshi'
k = 'i'
import re
patk = re.compile(k)
searchDone = False
sarr = []
startpos = 0
while(not searchDone):
    res = patk.search(S,startpos)
    if res == None:
        if len(sarr)==0:
            sarr.append((-1,-1))
        break
    else:
        #m = res.end()-res.start()-1
        if len(k) > 1:
            startpos = res.start()+len(k)-1
        else:
            startpos = res.start()+len(k)
        # if m > 1:
        #     last = res.start()
        #     for i in range(res.start(),res.end()):
        #         sarr.append((last,last+1))
        #         last += 1
        # else:
        sarr.append((res.start(),res.end()-1))
for i in sarr:
    print(i)