from itertools import combinations

#combinations by sorting str
a = list(map(str, input().split()))

b = a[0]
ss=[]
for strr in b:
    ss.append(strr)
ss.sort()
''.join(ss)
c = int(a[1])

store = []

for i in range(1, c + 1):
    result = list(combinations(ss, i))
    result.sort()

    for item in result:
        print(''.join(item))
#input example hack 2
#output
A
C
H
K
AC
AH
AK
CH
CK
HK
