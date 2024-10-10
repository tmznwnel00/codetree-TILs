from collections import defaultdict, deque

R, C, K = map(int, input().split())

m = [[0 for j in range(C)] for i in range(R+3)]
di2 = {}
entries = []
row_val = {}

def in_bounds(x, y):
    return 0 <= x < len(m) and 0 <= y < len(m[0])
def down(x, y, entry):
    # print(x, y)
    if x == 1:
        return (x, y, entry)
    if in_bounds(x-1, y-1) and in_bounds(x-1, y+1) and in_bounds(x-2, y) and m[x-1][y-1] == 0 and m[x-1][y+1] == 0 and m[x-2][y] == 0:
        return down(x-1, y, entry)
    elif in_bounds(x+1, y-1) and in_bounds(x, y-2) and in_bounds(x-1, y-1) and in_bounds(x-1, y-2) and in_bounds(x-2, y-1) and m[x+1][y-1] == 0 and m[x][y-2] == 0 and m[x-1][y-1] == 0 and m[x-1][y-2] == 0 and m[x-2][y-1] == 0:
        return down(x-1, y-1, (entry-1)%4)
    elif in_bounds(x+1, y+1) and in_bounds(x, y+2) and in_bounds(x-1, y+1) and in_bounds(x-1, y+2) and in_bounds(x-2, y+1) and m[x+1][y+1] == 0 and m[x][y+2] == 0 and m[x-1][y+1] == 0 and m[x-1][y+2] == 0 and m[x-2][y+1] == 0:
        return down(x-1, y+1, (entry+1)%4)
    else:
        return (x, y, entry)


def bfs(x, y):
    result = x
    q = deque([(x, y)])
    visit = set([(x, y)])

    while q:
        q_x, q_y = q.popleft()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in directions:
            new_x, new_y = q_x + dx, q_y + dy
            if in_bounds(new_x, new_y) and (new_x, new_y) not in visit and (((new_x, new_y) in di2 and
                    di2[(new_x, new_y)] == di2[(q_x, q_y)]) or (m[new_x][new_y] == 1 and (q_x, q_y) in entries)):
                q.append((new_x, new_y))
                visit.add((new_x, new_y))
                result = min(result, new_x)
    return result







answer = 0
for k in range(K):
    c, d = map(int, input().split())
    result = down(R+1, c-1, d%4)
    # print(result)
    if result[0] >= R-1:
        m = [[0 for j in range(C)] for i in range(R+3)]
        di2 = {}
        entries = []
        row_val = {}
    else:
        x, y = result[0], result[1]
        m[x][y], m[x+1][y], m[x-1][y], m[x][y+1], m[x][y-1] = 1, 1, 1, 1, 1
        di2[(x,y)] = (x,y)
        di2[(x+1, y)] = (x, y)
        di2[(x-1, y)] = (x, y)
        di2[(x, y+1)] = (x, y)
        di2[(x, y-1)] = (x, y)
        if result[2]%4 == 0:
            entries.append((x+1, y))
        elif result[2]%4 == 1:
            entries.append((x, y+1))
        elif result[2]%4 == 2:
            entries.append((x-1, y))
        elif result[2]%4 == 3:
            entries.append((x, y-1))

        result_row = bfs(x, y)
        answer += R - (result_row)


print(answer)