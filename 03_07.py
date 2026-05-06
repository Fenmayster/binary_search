import bisect

def solve():
    # 1. Читаємо кількість тваринок
    n = int(input())
    
    # 2. Читаємо їхні кольори (перетворюємо текст у список чисел)
    colors = list(map(int, input().split()))
    
    # 3. Читаємо кількість запитів
    m = int(input())
    
    # 4. Читаємо самі запити (які кольори треба перевірити)
    queries = list(map(int, input().split()))
    
    # Обробляємо кожен запит
    for q in queries:
        # Шукаємо ліву межу (перше входження)
        left = bisect.bisect_left(colors, q)
        
        # Шукаємо праву межу (відразу після останнього входження)
        right = bisect.bisect_right(colors, q)
        
        # Кількість елементів — це просто різниця між правою і лівою межею
        print(right - left)

# Запускаємо програму
if __name__ == '__main__':
    solve()