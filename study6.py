import testcase_study6
def minion_game(s):
    # your code goes here
    #quick shortcut for repeating substrings (symmetric)
    # total substrings of the count form 1+2+3+...+N = N(N+1)/2 
    # A ratio on subsequent iterations of repeating substrings
    # for repeating substring pattern can be determined for winner
    # A little algebraics can solve the winner for the Nth case
    # The ratio count between winner loser in symmetric strings should
    # be constant for subsequent base substring symmmetric repeat iterations
    # Determine the ratio ex. 72/48 = 1.5 for 'NANAN' iterated 4 times
    # 1.5*x + x = (N*N +N)/2 means x = (N**2 + N)/5
    # answer in winner case is 2*1.5 *x for Nth substring iteration
    ## avoids brute force time costs.
    def compute_palindromic_subset_win_count(N,win_count,loss_count):
        ratio_win_loss = win_count/loss_count
        return (N**2+N)/(1+ratio_win_loss)*ratio_win_loss

    def build_smallest_palindromic_pattern(s):
        st = ""
        for i in range(len(s)//2):
            if st == st[::-1] and len(st) >2:
                return st
            else:
                st+=s[i]
        return None

    def check_palindromic_subset(substr,s):
        substr_count = s.count(substr)
        print(substr)
        print(substr_count)
        if len(s)==substr_count*len(substr):
            return True
        return False


    scopy = s
    # substr = build_smallest_palindromic_pattern(s)
    palindromic_subset = False
    # if not substr == None:
    #     if check_palindromic_subset(substr,s):
    #         print(substr)
    #         scopy = substr
    #         palindromic_subset = True

    consonants = "bcdfghjklmnpqrstvwxyz".upper()
    vowels = "aeiou".upper()
    stumap = {}
    kevmap = {}
    #single char pass keyed by letter and valued by list indices
    for i,ch in enumerate(scopy):
        if ch in consonants:
            if ch in stumap:
                stumap[ch].append(i)
            else:
                stumap[ch] = [i]
        if ch in vowels:
            if ch in kevmap:
                kevmap[ch].append(i)
            else:
                kevmap[ch] = [i]
    ##main dicts tracks big substrings
    # stumapM = {}
    # kevmapM = {}
    stukevmaps = [stumap,kevmap]
    # stukevmapsM = [stumapM,kevmapM]
    # ## iterate single ch dicts above as forming basis index for substrings
    # for h, imap in enumerate(stukevmaps):
    #     for chkey in imap:
    #         clist = imap[chkey]
    #         for i in clist:
    #             N = len(s)-i-1 ## substring iteration length from index
    #             substr = chkey
    #             for j in range(N):
    #                 k = j+i
    #                 substr += s[k]
    #                 if substr in stukevmapsM[h]:
    #                     stukevmapsM[h][substr]+=1
    #                 else:
    #                     stukevmapsM[h][substr] = 1    # 
    countlist = [0, 0]
    for h, imap in enumerate(stukevmaps):
        for chkey in imap:
            clist = imap[chkey]
            for i in clist:
                N = len(scopy)-i ## substring iteration length from index
                player_count = countlist[h]
                player_count += N
                countlist[h] = player_count

    stucount = countlist[0]
    kevcount = countlist[1]
    wincount = max(stucount,kevcount)
    if palindromic_subset:
        winc = max(stucount,kevcount)
        lossc = min(stucount,kevcount)
        wincount = compute_palindromic_subset_win_count(len(scopy),winc,lossc)
    # for ch in stumap:
    #     stucount+=len(stumap[ch])
    # for substr in stumapM:
    #     stucount+=stumapM[substr]
    # kevcount = 0
    # for ch in kevmap:
    #     kevcount+=len(kevmap[ch])
    # for substr in kevmapM:
    #     kevcount+=kevmapM[substr]
    # print(len(s))
    # print(stucount)
    # print(kevcount)
    if stucount > kevcount:
        
        print("Stuart "+str(wincount))
    elif stucount == kevcount:
        print("Draw")
    else:
        print("Kevin "+str(wincount))
        
            

if __name__ == '__main__':
    s = input()
    minion_game(s)