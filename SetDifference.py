# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
set1=set(map(int,input().split()))
n=int(input())
set2=set(map(int,input().split()))
set1dif=list(set1.difference(set2))
set2dif=list(set2.difference(set1))
final=set1dif+set2dif
final.sort()
for i in final:
    print(i)
