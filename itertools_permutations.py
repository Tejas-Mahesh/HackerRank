# Enter your code here. Read input from STDIN. Print output to STDOUT
#does permutation of words useing itertools permutations
#input exampel hack 2
from itertools import permutations
a=list(map(str,input().split()))
result=list(permutations(a[0],int(a[1])))
result.sort()
for i in result:
    print(''.join(i))

#output AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
