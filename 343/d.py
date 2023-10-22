n, t = map(int, input().split())
S = [0] * n
d = {0: n}

for _ in range(t):
  a, b = map(int, input().split())
  a -= 1
  if S[a] in d:
    d[S[a]] -= 1
    if d[S[a]] == 0: d.pop(S[a])

  S[a] += b

  if S[a] in d: d[S[a]] += 1
  else: d[S[a]] = 1

  print(len(d))