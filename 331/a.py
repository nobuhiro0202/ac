M, D = map(int, input().split())
y, m, d = map(int, input().split())
if D == d:
    if M == m: print(y + 1, 1, 1)
    else: print(y, m + 1, 1)
else:
    print(y, m, d + 1)