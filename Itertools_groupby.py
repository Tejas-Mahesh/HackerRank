# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

for key, group in groupby(s):
    print((len(list(group)), int(key)), end=" ")
i#nput (stdin)
1222311
#Your Output (stdout)
(1, 1) (3, 2) (1, 3) (2, 1) 
#Expected Output
(1, 1) (3, 2) (1, 3) (2, 1)
