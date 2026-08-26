set1=set()
total_no=int(input())
for i in range(total_no):
    country=input()
    set1.add(country)
print(len(set1))


#Input (stdin)
7
UK
China
USA
France
New Zealand
UK
France
#Expected Output
5
#the set take only the unique value only
