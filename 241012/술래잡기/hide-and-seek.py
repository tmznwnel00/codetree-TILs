from collections import defaultdict
n, m, h, k = map(int, input().split())

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

users = []
trees = set([])
# sull.x, sull.y, sull_d = n//2, n//2, 3
lengths = {}

class User:
    def __init__(self, i, x, y, d):
        self.id = i
        self.x = x - 1
        self.y = y - 1
        self.d = d - 1
        self.deleted = False

class Sullae:
    def __init__(self):
        self.x = n // 2
        self.y = n // 2
        self.d = 3
        self.size = 1
        self.current_size = 0
        self.plus = 1

sull = Sullae()

for i in range(m):
    x, y, d = map(int, input().split())
    users.append(User(i, x, y, d))
    lengths[i] = abs(sull.x - x) + abs(sull.y - y)

for i in range(h):
    x, y = map(int, input().split())
    trees.add((x - 1, y - 1))

def check_in(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False

def user_move(user):
    if user.deleted:
        return
    if lengths[user.id] > 3:
        return
    new_x = user.x + dx[user.d % 4]
    new_y = user.y + dy[user.d % 4]
    if check_in(new_x, new_y):
        if new_x != sull.x or new_y != sull.y:
            user.x = new_x
            user.y = new_y
            lengths[user.id] = abs(sull.x - new_x) + abs(sull.y - new_y)
    else:
        user.d += 2
        new_x = user.x + dx[user.d % 4]
        new_y = user.y + dy[user.d % 4]
        if new_x != sull.x or new_y != sull.y:
            user.x = new_x
            user.y = new_y
            lengths[user.id] = abs(sull.x - new_x) + abs(sull.y - new_y)

def sull_move(sullae):
    new_x = sullae.x + dx[sullae.d % 4]
    new_y = sullae.y + dy[sullae.d % 4]
    if check_in(new_x, new_y):
        sullae.current_size += 1
        sullae.x = new_x
        sullae.y = new_y
    else:
        sullae.d += 2
        sullae.plus *= -1
        new_x = sullae.x + dx[sullae.d % 4]
        new_y = sullae.y + dy[sullae.d % 4]
        sullae.current_size = 2

    if sullae.current_size == sullae.size:
        if sullae.d % 4 == 0 and sullae.plus == 1:
            sullae.size += 1
        elif sullae.d % 4 == 1 and sullae.plus == -1:
            sullae.size -= 1
        sullae.d += 1
        sullae.current_size = 0

def sull_check(sullae):
    cnt = 0
    for i in range(3):
        new_x = sullae.x + dx[sullae.d % 4] * i
        new_y = sullae.y + dy[sullae.d % 4] * i
        if (new_x, new_y) in trees:
            continue
        if check_in(new_x, new_y):
            for user in users:
                if new_x == user.x and new_y == user.y and not user.deleted:
                    cnt += 1
                    user.deleted = True
    return cnt

answer = 0
for turn in range(k):
    for user in users:
        user_move(user)
    sull_move(sull)
    result = sull_check(sull)
    answer += (turn + 1) * result
print(answer)