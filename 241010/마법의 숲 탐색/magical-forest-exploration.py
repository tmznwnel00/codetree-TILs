from collections import defaultdict

R, C, K = map(int, input().split())

m = [[0 for j in range(C)] for i in range(R+3)]
di2 = {}
entries = {}
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

answer = 0
for k in range(K):
    c, d = map(int, input().split())
    result = down(R+1, c-1, d%4)
    # print(result)
    if result[0] >= R-1:
        m = [[0 for j in range(C)] for i in range(R+2)]
        di2 = {}
        entries = {}
    else:
        x, y = result[0], result[1]
        m[x][y], m[x+1][y], m[x-1][y], m[x][y+1], m[x][y-1] = 1, 1, 1, 1, 1
        di2[(x,y)] = (x,y)
        di2[(x+1, y)] = (x, y)
        di2[(x-1, y)] = (x, y)
        di2[(x, y+1)] = (x, y)
        di2[(x, y-1)] = (x, y)
        entries[(x, y)] = result[2]%4
        #행 추가..

        neighbors = defaultdict(list)
        if x == 1:
            pass
        else:
            if result[2] % 4 == 0:
                if in_bounds(x + 1, y + 1) and m[x + 1][y + 1] == 1:
                    neighbors[(x, y)].append(di2[(x + 1, y + 1)])
                if in_bounds(x + 2, y) and m[x + 2][y] == 1:
                    neighbors[(x, y)].append(di2[(x + 2, y)])
                if in_bounds(x + 1, y - 1) and m[x + 1][y - 1] == 1:
                    neighbors[(x, y)].append(di2[(x + 1, y - 1)])
            elif result[2] % 4 == 1:
                if in_bounds(x + 1, y + 1) and m[x + 1][y + 1] == 1:
                    neighbors[(x, y)].append(di2[(x + 1, y + 1)])
                if in_bounds(x, y + 2) and m[x][y + 2] == 1:
                    neighbors[(x, y)].append(di2[(x, y + 2)])
                if in_bounds(x - 1, y + 1) and m[x - 1][y + 1] == 1:
                    neighbors[(x, y)].append(di2[(x - 1, y + 1)])
            elif result[2] % 4 == 2:
                if in_bounds(x - 1, y + 1) and m[x - 1][y + 1] == 1:
                    neighbors[(x, y)].append(di2[(x - 1, y + 1)])
                if in_bounds(x - 2, y) and m[x - 2][y] == 1:
                    neighbors[(x, y)].append(di2[(x - 2, y)])
                if in_bounds(x - 1, y - 1) and m[x - 1][y - 1] == 1:
                    neighbors[(x, y)].append(di2[(x - 1, y - 1)])
            elif result[2] % 4 == 3:
                if in_bounds(x - 1, y - 1) and m[x - 1][y - 1] == 1:
                    neighbors[(x, y)].append(di2[(x - 1, y - 1)])
                if in_bounds(x, y - 2) and m[x][y - 2] == 1:
                    neighbors[(x, y)].append(di2[(x, y - 2)])
                if in_bounds(x + 1, y - 1) and m[x + 1][y - 1] == 1:
                    neighbors[(x, y)].append(di2[(x + 1, y - 1)])

        if (x, y) not in neighbors:
            answer += R-(x-1)
            row_val[(x,y)] = R-(x-1)
        else:
            max_val = 0
            for neighbor in neighbors[(x, y)]:
                if row_val[neighbor] > max_val:
                    max_val = row_val[neighbor]
            answer += max_val
            row_val[(x,y)] = max_val


print(answer)