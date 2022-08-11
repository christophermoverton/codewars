def print_rangoli(size):
    # your code goes here
    llist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z']
    rang_list = llist[0:size]
    N = size*2-1+(size-1)*2
    rang_list_rev = rang_list[0:]
    rang_list_rev.reverse()
    M = size*2-1
    srow = []
    lenrang = len(rang_list)
    for i in range(M//2+1):
        
        sublist = rang_list_rev[0:i+1]+rang_list[lenrang-i:lenrang] 
        rstr = ""
        for j,ch in enumerate(sublist):
            if j == len(sublist)-1:
                rstr += ch
            else:
                rstr += ch+"-"
        if i != M//2:
            srow.append(rstr)
        print(rstr.center(N,"-"))
    srow.reverse()
    for row in srow:
        print(row.center(N,"-"))    

n = 3
print_rangoli(n)