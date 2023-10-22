N = int(input())
S = ''.join(sorted(str(input())))

max_v = 10 ** N
ans = 0

i = 0
while i * i < max_v:
  T = ''.join(sorted(str(i * i))).zfill(N)
  if (S == T): ans += 1
  i += 1

print(ans)