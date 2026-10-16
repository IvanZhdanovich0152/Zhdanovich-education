import heapq

def prim(graph, start):
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)

    mst = []
    total = 0

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to in visited:
            continue
        visited.add(to)
        mst.append((frm, to, weight))
        total += weight
        for nxt, w in graph[to]:
            if nxt not in visited:
                heapq.heappush(edges, (w, to, nxt))

    return mst, total


graph1 = {
    1: [(2, 4), (5, 2), (4, 10)],
    2: [(1, 4), (3, 18), (4, 8)],
    3: [(2, 18), (4, 11), (8, 19)],
    4: [(1, 10), (2, 8), (3, 11), (5, 5), (7, 11), (8, 9)],
    5: [(1, 2), (4, 5), (6, 51)],
    6: [(5, 51), (7, 1), (8, 2)],
    7: [(4, 11), (6, 1), (8, 23)],
    8: [(3, 19), (4, 9), (6, 2), (7, 23)],
}

mst, total = prim(graph1, 1)
print("MST edges:")
for u, v, w in mst:
    print(f"  {u} -- {v} : {w}")
print(f"Total weight = {total}")