x = int(input())
a = x % 10
if a == 0: x = x // 10
else: x = (x // 10) + 1
print(x)