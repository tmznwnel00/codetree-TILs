import heapq
from collections import defaultdict, deque

Q = int(input())

nodes = [0] * 2001
edges = defaultdict(list)
products = {}
products_hq = []
deleted_products = set([])
costs = [101*10001] * 2001
started = set([0])
start = 0
costs[start] = 0

def make_cost():
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        edge = edges[node]
        for neighbor, weight in edge:
            if neighbor == start:
                continue
            if costs[neighbor] > costs[node] + weight:
                costs[neighbor] = costs[node] + weight
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

for q in range(Q):
    l = list(map(int, input().split()))
    t = l[0]

    if t == 100:
        n = l[1]
        m = l[2]

        for i in range(1, m + 1):
            v, u, w = l[i * 3], l[i * 3 + 1], l[i * 3 + 2]
            # edges[(u, v)] = w
            edges[u].append((v, w))
            edges[v].append((u, w))
        make_cost()

    elif t == 200:
        id, revenue, dest = l[1], l[2], l[3]
        products[id] = (revenue, dest)
        heapq.heappush(products_hq, (costs[dest] - revenue, id))

    elif t == 300:
        id = l[1]
        deleted_products.add(id)

    elif t == 400:
        result_product = None
        return_product = []
        while products_hq:
            product = heapq.heappop(products_hq)
            if product[1] in deleted_products:
                del products[product[1]]
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
        # if start not in started:
        #     # 다시 cost 산정
        #     pass