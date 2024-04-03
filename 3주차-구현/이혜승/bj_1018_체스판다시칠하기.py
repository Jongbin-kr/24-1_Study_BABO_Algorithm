# 8*8 크기의 체스판으로 만들려고 한다. 검은색과 흰색이 번갈아서 칠해서 있어야 한다. 
# 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠하기

N, M = map(int,input().split())
board = []
result = []


for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        draw1 = 0
        draw2 = 0

        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        
        result.append(draw1)
        result.append(draw2)

print(min(result))

