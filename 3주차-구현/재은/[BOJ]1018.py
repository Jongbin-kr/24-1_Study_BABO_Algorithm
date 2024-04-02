N, M = map(int, input().split())

chessboard = [list(input()) for _ in range(N)]

def check_boxes(cur, start):
    cnt = 0
    cnt2 = 0
    new_map = []
    for p in cur:
        new_map.append(p[start:start+8])

    flag = 'W'
    flag2 = 'B'
    #flag를 W로 설정하는 경우, B로 설정하는 경우 두가지로 나누기

    for j in range(8):
        for i in range(8):
            if (j+i)%2==0:
                if flag==new_map[j][i]:
                    continue
                else:
                    cnt += 1
                    continue
            else:
                if flag!=new_map[j][i]:
                    continue
                else:
                    cnt+=1
                    continue
    for j in range(8):
        for i in range(8):
            if (j+i)%2==0:
                if flag2==new_map[j][i]:
                    continue
                else:
                    cnt2 += 1
                    continue
            else:
                if flag2!=new_map[j][i]:
                    continue
                else:
                    cnt2+=1
                    continue
    return min(cnt,cnt2)

result = []

for i in range(N-7):
    cur = chessboard[i:i+8]
    for start in range(M-7):
        cnt = check_boxes(cur, start)
        result.append(cnt)

print(min(result))
