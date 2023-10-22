import math

n = int(input())
A = list(map(int, input().split()))

def T(n):
  if 0 <= n < 3: return n;
  b = int(n ** .5)
  a = None;
  for i in range(b, 0, -1):
    if (n / (i ** 2)).is_integer():
      a = int(n / (i ** 2))
      break
  return a

d = {}

for i in range(n): A[i] = T(A[i])
z = [a for a in A if a == 0]
A = [a for a in A if a != 0]
A.sort()

for a in A:
  if a not in d: d[a] = 1
  else: d[a] += 1

ans = math.comb(len(z), 2)
ans += len(A) * len(z)

for k in d: ans += math.comb(d[k], 2)

print(ans)