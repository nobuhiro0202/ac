import math
N = int(input())
a = 0
c = N
while a == 0:
  i = str(c)
  if int(i[-3]) * int(i[-2]) == int( i[-1]): a = c
  c += 1

print(a)