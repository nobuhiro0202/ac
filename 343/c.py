n = int(input())
r = int(n ** (1 / 3))

def check(n):
  return str(n) == str(n)[::-1]

i = 1
ans = 1
while i ** 3 <= n:
  if check(i ** 3): ans = i ** 3
  i += 1

print(ans)