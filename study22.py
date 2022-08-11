import operator
import testcase_study22

def person_lister(f):
    def inner(people):
        # complete the function
        ol = []
        list_tuple = [tuple(i) for i in people]
        sort_list_tuple = sorted(list_tuple, key=lambda x:int(x[2]))
        #print(sort_list_tuple)
        for person in sort_list_tuple:
            ostr = f(person)
            ol.append(ostr)
        return ol
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    n = int(input())
    people = [input().split() for i in range(n)]
    outans = name_format(people)
    print(*outans, sep='\n')
    import testcase_study22_out
    for i in range(n):
        exans = input()
        if exans != outans[i]:
            print('expected: '+str(exans))
            print('outans: '+ str(outans[i]))