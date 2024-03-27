# 성능
시간 44ms


# 코드

```python
n=int(input())
w=[int(num) for num in input().split()]
w.sort()
answer=[w[i]+w[-(1+i)] for i in range(n)]
print(min(answer))
```
