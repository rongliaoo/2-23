'''
set1 = {2,4,6,8,10}
list = list(set1)
print(list)
for i in set1:
    print(i,end =' ')

'''
WF = {"Angel Falls" : 3211.7, "Tugela Falls" : 3110.2,
 "Three Sisters Fall" : 2998.5,"Olo falls":2953.3, "Yumbilla Falls":2940}
#print(list(WF.keys()))
#print(list(WF.values()))
#print(list(WF.items()))

for x in WF.items():
    print(x)
    print(x[1])
