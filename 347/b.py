s = input()
a = []
for i in range(len(s)):
  for j in range(i + 1, len(s) + 1):
    if not s[i:j] in a: a.append(s[i:j])
    
print(len(a))