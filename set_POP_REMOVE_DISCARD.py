n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    operation = input().split()

    if operation[0] == "pop":
        s.pop()

    elif operation[0] == "remove":
        s.remove(int(operation[1]))

    elif operation[0] == "discard":
        s.discard(int(operation[1]))

print(sum(s))
#nput (stdin)
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Your Output (stdout)
4
Expected Output
4
