import math
def justify(text, width):
    def wsarr(wscount, wswcount):
        ## whitsepace characters count , whitespace word count
        rwsarr = []
        for i in range(0,wswcount):
            rwsarr.append('')
        for i in range(0,wscount):
            rwsarr[i%wswcount] += ' '
        return rwsarr     
    # your code here
    tsplit = text.split()
    print(tsplit)
    count = 0
    wpluscount = 0
    substr = []
    rstr = ''
    print(width)
    print(text)
    for word in tsplit:        
        if len(word)+wpluscount <= width:
            substr.append(word)
            count += len(word)
            wpluscount += len(word)+1
            
        else:
            wsc = width - count
            wswordcnt = len(substr)-1
            wslist = []
            line = ''
            if (wswordcnt == 0):
                wscstr = ''
                for l in range(0,wsc):
                    wscstr += ' '
                line += substr[0]
            else:
                wslist = wsarr(wsc,wswordcnt)
            
                for i, subword in enumerate(substr):
                    if i == 0:
                        line += subword
                    else:
                        line += wslist[i-1]+subword
            line += '\n'
            rstr += line
            line = ''
            substr = [word]
            count = len(word)
            wpluscount = len(word)+1
            ##div = round(wsc/(wordcnt-1))
            ##tval = math.floor(wsc / div)
    
    for i, word in enumerate(substr):
        if i != len(substr)-1:
            rstr += word +' ' 
        else:
            rstr += word
    print(rstr)
    return rstr

txtstrng = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.'
newstring = justify(txtstrng,15)
print('hi')
print(newstring)