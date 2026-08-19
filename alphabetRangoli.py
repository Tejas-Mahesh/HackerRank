def print_rangoli(size):
    # your code goes here
    for i in range(n):
        letters = [chr(ord('a') + j) for j in range(n - 1, n - i - 2, -1)]
        letters += [chr(ord('a') + j) for j in range(n - i, n)]

        print("--" * (n - i - 1) + "-".join(letters) + "--" * (n - i - 1))

    for i in range(n - 2, -1, -1):
        letters = [chr(ord('a') + j) for j in range(n - 1, n - i - 2, -1)]
        letters += [chr(ord('a') + j) for j in range(n - i, n)]

        print("--" * (n - i - 1) + "-".join(letters) + "--" * (n - i - 1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
