import heapq

N, M, P, C, D = map(int, input().split())
r_r, r_c = map(int, input().split())
r_r -= 1
r_c -= 1

plate = [[0 for _ in range(N)] for _ in range(N)]
plate[r_r][r_c] = 'R'

scores = [0 for _ in range(P)]

santas = {}

for p in range(P):
    p_n, s_r, s_c = map(int, input().split())
    santas[p_n - 1] = (s_r - 1, s_c - 1)
    plate[s_r - 1][s_c - 1] = 'S'

hq = []
direction = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
stunned1, stunned2 = set([]), set([])

def path_length():
    for santa in santas.values():
        length = (r_r - santa[0]) ** 2 + (r_c - santa[1]) ** 2
        heapq.heappush(hq, (length, -santa[0], -santa[1]))
path_length()

def check_move(x, y):
    if x >= N or x < 0 or y >= N or y < 0:
        return False
    else:
        return True

def move(sp_r, sp_c, santa, d, size):
    # 충돌 + 상호작용
    move_r, move_c = sp_r + direction[d][0] * size, sp_c + direction[d][1] * size
    if move_r >= N or move_r < 0 or move_c >= N or move_c < 0:
        pass
    else:
        for new_santa, (dict_r, dict_c) in santas.items():
            if move_r == dict_r and move_c == dict_c:
                move(move_r, move_c, new_santa, d, 1)
        santas[santa] = (move_r, move_c)

def move_santa(r_r, r_c, s_r, s_c):
    d_list = []
    if r_r > s_r:
        if r_c > s_c:
            d_list.append((1, 0))
            d_list.append((0, 1))
        elif r_c < s_c:
            d_list.append((1, 0))
            d_list.append((0, -1))
        else:
            d_list.append((1, 0))
    elif r_r < s_r:
        if r_c > s_c:
            d_list.append((-1, 0))
            d_list.append((0, 1))
        elif r_c < s_c:
            d_list.append((-1, 0))
            d_list.append((0, -1))
        else:
            d_list.append((-1, 0))
    else:
        if r_c > s_c:
            d_list.append((0, 1))
        elif r_c < s_c:
            d_list.append((0, -1))

    new_x, new_y = s_r, s_c
    d = None

    min_val = abs(r_r-new_x)**2 + abs(r_c-new_y)**2

    for d_x, d_y in d_list:
        if (d_x, d_y) == (-1, 0):
            if check_move(new_x - 1, new_y) == False or (new_x - 1, new_y) in santas.values():
                continue
            else:
                if abs(r_r-(new_x-1))**2 + abs(r_c-new_y)**2 < min_val:
                    min_val = abs(r_r-(new_x-1))**2 + abs(r_c-(new_y))**2
                    d = 0
        elif (d_x, d_y) == (0, 1):
            if check_move(new_x, new_y + 1) == False or (new_x, new_y + 1) in santas.values():
                continue
            else:
                if abs(r_r - new_x) ** 2 + abs(r_c - (new_y+1)) ** 2 < min_val:
                    min_val = abs(r_r - new_x) ** 2 + abs(r_c - (new_y+1)) ** 2
                    d = 6
        elif (d_x, d_y) == (1, 0):
            if check_move(new_x + 1, new_y) == False or (new_x + 1, new_y) in santas.values():
                continue
            else:
                if abs(r_r - (new_x + 1)) ** 2 + abs(r_c - new_y) ** 2 < min_val:
                    min_val = abs(r_r - (new_x + 1)) ** 2 + abs(r_c - (new_y)) ** 2
                    d = 4
        elif (d_x, d_y) == (0, -1):
            if check_move(new_x, new_y - 1) == False or (new_x, new_y - 1) in santas.values():
                continue
            else:
                if abs(r_r - new_x) ** 2 + abs(r_c - (new_y-1)) ** 2 < min_val:
                    min_val = abs(r_r - new_x) ** 2 + abs(r_c - (new_y - 1)) ** 2
                    d = 2
    if d == 0:
        new_x, new_y = new_x - 1, new_y
    elif d == 2:
        new_x, new_y = new_x, new_y - 1
    elif d == 4:
        new_x, new_y = new_x + 1, new_y
    elif d == 6:
        new_x, new_y = new_x, new_y + 1

    return new_x, new_y, d

for m in range(M):
    if not hq:
        break
    path = heapq.heappop(hq)

    # 루돌프 움직이고 충돌 처리
    s_r, s_c = -path[1], -path[2]
    if r_r > s_r:
        if r_c > s_c:
            r_r -= 1
            r_c -= 1
            d = 5
        elif r_c < s_c:
            r_r -= 1
            r_c += 1
            d = 3
        else:
            r_r -= 1
            d = 4
    elif r_r < s_r:
        if r_c > s_c:
            r_r += 1
            r_c -= 1
            d = 7
        elif r_c < s_c:
            r_r += 1
            r_c += 1
            d = 1
        else:
            r_r += 1
            d = 0
    else:
        if r_c > s_c:
            r_c -= 1
            d = 6
        elif r_c < s_c:
            r_c += 1
            d = 2

    for santa, (sp_r, sp_c) in santas.items():
        if r_r == sp_r and r_c == sp_c:
            del santas[santa]
            scores[santa] += C
            move(sp_r, sp_c, santa, d, C)
            stunned1.add(santa)
            stunned2.add(santa)
            break

    # 산타 움직이고 충돌 처리
    santa_list = sorted(list(santas.keys()))
    for santa in santa_list:
        if santa in stunned1:
            continue
        s_r, s_c = santas[santa]
        move_r, move_c, d = move_santa(r_r, r_c, s_r, s_c)
        del santas[santa]
        if move_r == r_r and move_c == r_c:
            scores[santa] += D
            move(move_r, move_c, santa, d, D)
            stunned2.add(santa)
        else:
            santas[santa] = (move_r, move_c)

    stunned1, stunned2 = stunned2, set([])
    hq = []

    for santa in santas.values():
        length = (r_r - santa[0]) ** 2 + (r_c - santa[1]) ** 2
        heapq.heappush(hq, (length, -santa[0], -santa[1]))
    for santa in santas.keys():
        scores[santa] += 1


print(" ".join(map(str, scores)))