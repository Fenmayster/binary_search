import math

def solve():
    left = 1.6
    right = 3.0
    
    for i in range(100):
        mid = (left + right) / 2
        val = math.sin(mid) - mid / 3
        
        if val > 0:
            left = mid
        else:
            right = mid
            
    print(f"{left:.6f}")

if __name__ == '__main__':
    solve()