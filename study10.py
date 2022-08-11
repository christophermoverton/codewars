import re
pat = r"([A-Za-z0-9])\1(?<=[A-Za-z0-9]\1){1}"
S = "__commit__"
matchS =  re.search(pat,S)
if matchS != None:
    print(matchS.group(1))
    
#print(re.search(pat,S).group(0))
#print(re.findall(pat,S))