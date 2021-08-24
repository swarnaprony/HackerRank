if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort(reverse=True)
    runnerup = arr[1]
    print(runnerup)
