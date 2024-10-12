n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2
start = 1
mapping = {}
mapping[(x, y)] = 0

direction = 0
index = 0
cnt = 0
while start < n:
    index += 1
    new_x, new_y = x + dx[direction], y + dy[direction]
    mapping[(new_x, new_y)] = index
    cnt += 1
    x, y = new_x, new_y

    if cnt == start:
        if direction % 2 == 1:
            start += 1
        direction = (direction + 1) % 4
        cnt = 0

for i in range(n - 1):
    mapping[(0, i)] = n ** 2 - i - 1

sequence = [0 for _ in range(n ** 2)]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        sequence[mapping[(i, j)]] = l[j]



x, y = n // 2, n // 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
for _ in range(m):
    d, p = map(int, input().split())
    del_index = []
    current_x, current_y = x, y
    for i in range(1, p + 1):
        new_x, new_y = current_x + dx[d], current_y + dy[d]
        if sequence[mapping[(new_x, new_y)]] != 0:
            del_index.append(mapping[(new_x, new_y)])
        current_x, current_y = new_x, new_y

    for j in range(len(del_index)):
        answer += sequence[del_index[-1 -j]]
        del sequence[del_index[-1 -j]]

    current_num = 0
    start_index = 0
    current_index = 1
    cnt = 0
    while True:
        if current_index >= len(sequence):
            break
        if sequence[current_index] == 0:
            break
        else:
            if sequence[current_index] != current_num:
                if cnt >= 4:
                    for k in range(current_index - 1, start_index - 1, - 1):
                        answer += sequence[k]
                        del sequence[k]
                    current_num = 0
                    start_index = 0
                    current_index = 1
                    cnt = 0
                else:
                    current_num = sequence[current_index]
                    cnt = 1
                    start_index = current_index
                    current_index += 1
            else:
                cnt += 1
                current_index += 1

    new_sequence = [0]

    cnt = 0
    current_num = sequence[1]
    index = 1
    while True:
        if sequence[index] == 0:
            break
        if current_index >= len(sequence):
            break
        if sequence[index] != current_num:
            new_sequence.append(cnt)
            new_sequence.append(current_num)
            cnt = 1
            current_num = sequence[index]
        else:
            cnt += 1
        index += 1

    new_sequence.append(cnt)
    new_sequence.append(current_num)

    while len(new_sequence) < n ** 2:
        new_sequence.append(0)

    while len(new_sequence) > n ** 2:
        new_sequence.pop()


    sequence = new_sequence

print(answer)