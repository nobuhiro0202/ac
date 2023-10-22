N, S = input().split()
A = [input() for _ in range(int(N))]

def oneEditAway(first, second):
  if abs(len(first) - len(second)) > 1: return False
  s1 = first if len(first) < len(second) else second
  s2 = second if len(first) < len(second) else first
  x1 = 0
  x2 = 0
  foundDifference = False
  while x2 < len(s2) and x1 < len(s1):
    if s1[x1] != s2[x2]:
      if (foundDifference): return False
      foundDifference = True
      if len(s1) == len(s2): x1 += 1
    else: x1 += 1
    x2 += 1
  return True

ns = []
for index, str in enumerate(A):
  if oneEditAway(S, str): ns.append(index + 1)

print(len(ns))
print(*ns)