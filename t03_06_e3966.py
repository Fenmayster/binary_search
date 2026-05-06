def solve(array, x):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2  
        if array[mid] == x:
            return "YES"
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return "NO"


n = int(input())
array = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    print(solve(array, q))