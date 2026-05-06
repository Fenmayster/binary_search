import bisect

def solve():
    n = int(input())
    colors = list(map(int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))
    
    for q in queries:
        left = bisect.bisect_left(colors, q)
        right = bisect.bisect_right(colors, q)
        print(right - left)

if __name__ == '__main__':
    solve()