N, M = map(int, input().split())

chessboard = [list(input()) for _ in range(N)]

def check_W(new_map):
    for j in range(8):
        for i in range(8):
            if (j+i)%2==0:
                if 'W'==new_map[j][i]:
                    continue
                else:
                    cnt += 1
                    continue
            else:
                if 'W'!=new_map[j][i]:
                    continue
                else:
                    cnt+=1
                    continue
    return cnt

def check_B(new_map):
    for j in range(8):
        for i in range(8):
            if (j+i)%2==0:
                if 'B'==new_map[j][i]:
                    continue
                else:
                    cnt += 1
                    continue
            else:
                if 'B'!=new_map[j][i]:
                    continue
                else:
                    cnt+=1
                    continue
    return cnt

def check_boxes(cur, start):
    cnt = 0
    new_map = []
    for p in cur:
        new_map.append(p[start:start+8])
    flag = new_map[0][0]
    if flag=='W':
        cnt_W = check_W(new_map)
    elif flag=='B':
        cnt_B = check_B(new_map)
    
    return min(cnt_W, cnt_B)
    # # for j in range(8):
    # #     cur = map[j]

    # #     if (i%2==0 and j%2==0):
    # #         if cur==flag:
    # #             continue
    # #         else:
    # #             cnt +=1
    # #             continue
    # #     if (i%2==1 and j%2==1):
    # #         if cur==flag:
    # #             continue
    # #         else:
    # #             cnt +=1
    # #             continue
    # #     if ((i%2)!=(j%2)):
    # #         if cur!=flag:
    # #             continue
    # #         elif cur==flag:
    # #             cnt+=1
    # #             continue
    # return cnt

result = []

for i in range(N-7):
    cur = chessboard[i:i+8]
    for start in range(M-7):
        cnt = check_boxes(cur, start)
        result.append(cnt)

print(min(result))
