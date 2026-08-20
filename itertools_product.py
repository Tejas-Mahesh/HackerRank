from itertools import product
#product of lists useing itertools product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*list(product(a,b)))
