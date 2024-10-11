import heapq
from collections import defaultdict

Q = int(input())

nodes = [0] * 2001
edges = defaultdict(list)
products = {}
products_hq = []
deleted_products = set([])
costs = [101 * 10001] * 2001
start = 0
costs[start] = 0

def make_cost():
    pq = [(0, start)]  # (cost, node)
    costs[start] = 0

    while pq:
        current_cost, node = heapq.heappop(pq)
        if current_cost > costs[node]:
            continue

        for neighbor, weight in edges[node]:
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
            # 중복 간선 처리
            edge_updated = False
            for idx, (neighbor, weight) in enumerate(edges[u]):
                if neighbor == v and weight > w:
                    edges[u][idx] = (v, w)
                    edge_updated = True
                    break
            if not edge_updated:
                edges[u].append((v, w))

            edge_updated = False
            for idx, (neighbor, weight) in enumerate(edges[v]):
                if neighbor == u and weight > w:
                    edges[v][idx] = (u, w)
                    edge_updated = True
                    break
            if not edge_updated:
                edges[v].append((u, w))
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
            if product[1] in products:
                if product[0] <= 0:
                    print(product[1])
                    del products[product[1]]
                    result_product = product
                    break
            else:
                continue

        if result_product is None:
            print(-1)

    elif t == 500:
        s = l[1]
        start = s
        costs = [101 * 10001] * 2001
        costs[start] = 0
        make_cost()

        new_products_hq = []
        for id, (revenue, dest) in products.items():
            if costs[dest] != 101 * 10001 and revenue >= costs[dest]:
                heapq.heappush(new_products_hq, (costs[dest] - revenue, id))

        products_hq = new_products_hq