from string import ascii_lowercase
n = int(input())
s = input()
q = int(input())

mapping_from = ascii_lowercase
mapping_to = ascii_lowercase

for i in range(q):
  c, d = input().split()
  mapping_to = mapping_to.replace(c, d)

print(s.translate(str.maketrans(mapping_from, mapping_to)))