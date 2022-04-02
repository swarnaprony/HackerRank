def miniMaxSum(arr):
    # Write your code here
    max = arr[0]
    min_sum = 0
    max_sum = 0
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > min:
            max_sum = max_sum + arr[i]
        else:
            max_sum = max_sum + min
            min = arr[i]
        if arr[i] < max:
            min_sum = min_sum + arr[i]
        else:
            min_sum = min_sum + max
            max = arr[i]
    return print(f"{min_sum} {max_sum}")
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)