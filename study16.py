import testcase_study16
import numpy
n,m = map(int, input().split())
nmarr = []
for i in range(n):
    mlist = list(map(int, input().split()))
    nmarr.append(mlist)
my_array = numpy.array(nmarr)    
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis= 0))
x = numpy.std(my_array, axis=None)
format_float = "{:.11f}".format(x)
if (abs(float(format_float)) < 1e-12):
    print(0.0)
else:
    print(format_float)