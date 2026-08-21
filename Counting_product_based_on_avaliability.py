# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())

shoes = list(map(int, input().split()))

shoe_count = Counter(shoes)

customers = int(input())

money = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        money += price
        shoe_count[size] -= 1

print(money)
#input
10
2 3 4 5 6 8 7 6 5 18 #for this use Counter
6
6 55
6 45
6 55
4 40
18 60
10 50
#Expected Output
200
            
     
