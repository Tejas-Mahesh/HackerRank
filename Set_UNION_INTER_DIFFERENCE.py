# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
m=int(input())
set2=set(map(int,input().split()))
final=set1.union(set2)
print(len(final))
#input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
#Expected Output
13

set1.intersection(set2)
set1.difference(set2)
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
m=int(input())
set2=set(map(int,input().split()))
total=set1.intersection(set2)
print(len(total))
