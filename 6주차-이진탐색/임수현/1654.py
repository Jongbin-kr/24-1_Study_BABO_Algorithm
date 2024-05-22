import sys

n,m=map(int,input().split())

def cut(length):
    cuts=[lan//length for lan in lans]
    return sum(cuts)

lans=[]
for _ in range(n):
    lans.append(int(sys.stdin.readline()))
high=max(lans)
low=1


while low<=high:
    length=(high+low)//2
    total_cuts=cut(length)

    if total_cuts<m:
        high=length-1
    else:
        low=length+1
print(high)
