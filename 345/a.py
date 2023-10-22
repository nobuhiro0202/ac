s = input()
b = True
if not (s[0] == '<' and s[-1] == '>'): b = False
for i in range(1, len(s) - 1):
  if not b: break
  if s[i] != '=': b = False
if b: print('Yes')
else: print('No')