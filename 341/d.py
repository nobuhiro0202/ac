n, m, k = map(int, input().split())

found = 0
num = min(n, m)
while found < k:
  if num % n == 0 or num % m == 0:
    if not (num % n == 0 and num % m == 0):
      found += 1
      if found == k: break
        
  num += 1

print(num)