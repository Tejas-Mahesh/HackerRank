n=int(input())
names=[]
for i in range(n):
    names.append(input())
for i in names:
    even=i[::2]
    odd=i[1::2]
    print(even ,odd)
#this divide the string based on even and odd 
