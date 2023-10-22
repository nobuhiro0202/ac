n = int(input())
for i in range(n):
  l = list(map(int, input().split()))
  a = []
  for index, e in enumerate(l):
    if e == 1: a.append(index + 1)
  print(*a)
  