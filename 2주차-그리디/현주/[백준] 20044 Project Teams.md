# 백준20044번 Project Teams
```python
n = int(input())
m = list(map(int, input().split()))
a = sorted(m)
b = sorted(m, reverse=True)
arr = []
for i in range(len(m)):
    x = a[i] + b[i]
    arr.append(x)
    
print(min(arr))
```
