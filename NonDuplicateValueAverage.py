def average(array):
    # your code goes here
    store=[]
    for i in array:
        if i not in store:
            store.append(i)
    size=len(store)
    average=sum(store)/size
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
