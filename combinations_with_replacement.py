# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()

s = sorted(s)

for combination in combinations_with_replacement(s, int(k)):
    print(''.join(combination))
#input
HACK 2
#Expected Output
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
