def solve():

    left = 0.0
    right = 2.0
    
    for i in range(100):
        mid = (left + right) / 2
        val = mid**3 + 4 * (mid**2) + mid - 6
        if val < 0:
            left = mid
        else:
            right = mid
            
    print(f"{left:.6f}")

if __name__ == '__main__':
    solve()