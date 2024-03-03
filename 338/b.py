from collections import Counter
d = Counter(input())
m = max(d.values())
mi = [key for key, count in d.items() if count == m]
print(min(mi))