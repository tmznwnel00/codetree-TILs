from collections import deque

n, m = map(int, input().split())

board = []
dice = [1, 2, 3, 4, 5, 6]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
df, dr, dc = 6, 3, 2
direction = 0
dice_x, dice_y = 0, 0

for i in range(n):
    board.append(list(map(int, input().split())))

visited = set([])
scores = [[0 for _ in range(n)] for _ in range(n)]

def is_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(n):
    for j in range(n):
        if (i, j) in visited:
            continue
        visited.add((i, j))
        dq = deque([(i, j)])
        score = 0
        history = set([])
        l = [(i, j)]
        while dq:
            p = dq.popleft()
            for d in range(4):
                new_x, new_y = p[0] + dx[d], p[1] + dy[d]
                if (new_x, new_y) in history:
                    continue
                if is_range(new_x, new_y):
                    history.add((new_x, new_y))
                    if board[i][j] == board[new_x][new_y]:
                        score += 1
                        l.append((new_x, new_y))
                        dq.append((new_x, new_y))
                        visited.add((new_x, new_y))
        for vx, vy in l:
            scores[vx][vy] = max(1, score)

answer = 0
for _ in range(m):
    new_x, new_y = dice_x + dx[direction % 4], dice_y + dy[direction % 4]
    if is_range(new_x, new_y):
        answer += board[new_x][new_y] * scores[new_x][new_y]
        if direction % 4 == 0:
            df, dr, dc = dr, 7 - df, dc
        elif direction % 4 == 1:
            df, dr, dc = dc, dr, 7 - df
        elif direction % 4 == 2:
            df, dr, dc = 7 - dr, df, dc
        else:
            df, dr, dc = 7 - dc, dr, df

        if df > board[new_x][new_y]:
            direction += 1
        elif df < board[new_x][new_y]:
            direction -= 1
    else:
        direction += 2
        new_x, new_y = dice_x + dx[direction % 4], dice_y + dy[direction % 4]
        answer += board[new_x][new_y] * scores[new_x][new_y]

        if direction % 4 == 0:
            df, dr, dc = dr, 7 - df, dc
        elif direction % 4 == 1:
            df, dr, dc = dc, dr, 7 - df
        elif direction % 4 == 2:
            df, dr, dc = 7 - dr, df, dc
        else:
            df, dr, dc = 7 - dc, dr, df
        if df > board[new_x][new_y]:
            direction += 1
        elif df < board[new_x][new_y]:
            direction -= 1
    dice_x, dice_y = new_x, new_y

print(answer)