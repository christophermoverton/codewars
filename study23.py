
listn = [1,2,3,4,5,-9]
print(any([int(str(abs(i))[::-1]) == i for i in listn]) and all([i>0 for i in listn]))

strng = "Sorting1234"
f_1 = [lambda l: (l.islower(),l),lambda l: (l.isupper(),l),
       lambda l: l.isdigit() and int(l)%2==0, lambda l: l.islower()<l.isupper(),
       lambda l: l.isupper() < l.isdigit()]
strng1 = strng[0:]
for i in f_1: 
    strng = sorted(strng, key=i)
print(strng)
print(sorted(strng1,key=f_1[0]))