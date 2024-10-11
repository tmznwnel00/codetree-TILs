import heapq
from collections import defaultdict, deque

Q = int(input())

nodes = [0] * 2001
edges = defaultdict(list)
edges2 = defaultdict(int)
products = {}
products_hq = []
deleted_products = set([])
costs = [101*10001] * 2001
started = set([0])
start = 0
costs[start] = 0

# def make_cost():
#     visited = set([start])
#     q = deque([start])
#
#     while q:
#         node = q.popleft()
#         edge = edges[node]
#         for neighbor, weight in edge:
#             if neighbor == start:
#                 continue
#             if costs[neighbor] > costs[node] + weight:
#                 costs[neighbor] = costs[node] + weight
#             if neighbor not in visited:
#                 q.append(neighbor)
#                 visited.add(neighbor)

def make_cost():
    pq = [(0, start)]  # (cost, node)
    visited = set([start])
    costs[start] = 0

    while pq:
        current_cost, node = heapq.heappop(pq)
        if current_cost > costs[node]:
            continue

        for neighbor, weight in edges[node]:
            if neighbor in visited:
                continue
            new_cost = current_cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))


for q in range(Q):
    l = list(map(int, input().split()))
    t = l[0]

    if t == 100:
        n = l[1]
        m = l[2]

        for i in range(1, m + 1):
            v, u, w = l[i * 3], l[i * 3 + 1], l[i * 3 + 2]
            if (u, v) in edges2 and edges2[(u, v)] < w:
                continue
            else:
                edges[u].append((v, w))
                edges[v].append((u, w))
                edges2[(u, v)] = w
        make_cost()

    elif t == 200:
        id, revenue, dest = l[1], l[2], l[3]
        products[id] = (revenue, dest)
        heapq.heappush(products_hq, (costs[dest] - revenue, id))

    elif t == 300:
        id = l[1]
        if id in products:
            del products[id]

    elif t == 400:
        result_product = None
        return_product = []
        while products_hq:
            product = heapq.heappop(products_hq)
            if product[1] not in products:
                continue
            elif product[0] > 0:
                return_product.append(product)
            else:
                deleted_products.add(product[1])
                del products[product[1]]
                result_product = product
                break
        if result_product:
            print(result_product[1])
        else:
            print(-1)

        for product in return_product:
            heapq.heappush(products_hq, product)

    elif t == 500:
        s = l[1]
        start = s
        costs = [101 * 10001] * 2001
        costs[start] = 0
        make_cost()

        products_hq = []

        for id, (revenue, dest) in products.items():
            if costs[dest] == 101 * 10001:
                pass
            elif revenue >= costs[dest]:
                heapq.heappush(products_hq, (costs[dest] - revenue, id))