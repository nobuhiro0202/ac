n = int(input())
a = 0
b = 0
a, b = map(int, input().split())
for i in range(1, n): 
    x, y = map(int, input().split())
    a += x
    b += y
if a > b: print('Takahashi')
if a < b: print('Aoki')
if a == b: print('Draw')