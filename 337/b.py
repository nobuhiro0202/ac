s = input()
ca = cb = cc = 0

arr = []
cur = ""

for char in s:
    if not cur or char == cur[0]: cur = char
    else:
        arr.append(cur)
        cur = char
if cur: arr.append(cur)
    
if len(arr) > 3 or len(arr) == 0: print('No')
else: 
    if len(arr) == 3:
        if ('A' in arr[0] and 'B' in arr[1] and 'C' in arr[2]): print("Yes")
        else: print('No')
    if len(arr) == 2:
        if ('A' in arr[0] and 'B' in arr[1]) or ('A' in arr[0] and 'C' in arr[1]) or ('B' in arr[0] and 'C' in arr[1]): print("Yes")
        else: print("No")
    if len(arr) == 1:
        if any(char in arr[0] for char in ['A', 'B', 'C']): print("Yes")
        else: print("No")