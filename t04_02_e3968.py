import math

def solve():
    c = float(input())
    left = 0.0
    right = 100000.0
    
    for i in range(100):
        mid = (left + right) / 2
        val = mid * mid + math.sqrt(mid)
        if val < c:
            left = mid
        else:
            right = mid
    print(f"{left:.10f}")

if __name__ == '__main__':
    solve()