s = input()
d = {}
u = None
for i in range(len(s)):
  if s[i] not in d: d[s[i]] = 1
  else: d[s[i]] += 1
for key, value in d.items():
    if value == 1: u = key

for i in range(len(s)):
  if s[i] == u: print(i + 1)