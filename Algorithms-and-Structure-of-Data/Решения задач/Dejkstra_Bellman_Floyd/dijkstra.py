import heapq

EDGES = [
    ('s', 'a', 2),
    ('s', 'c', 5),
    ('s', 'd', 1),
    ('a', 'b', 2),
    ('a', 'f', 2),
    ('a', 'g', 1),
    ('b', 'c', 2),
    ('b', 'g', 4),
    ('c', 't', 3),
    ('d', 'f', 1),
    ('f', 'g', 2),
    ('g', 't', 6),
]
START, TARGET = 's', 't'

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        distance, u = heapq.heappop(pq)
        if distance > dist[u]:
            continue
        for v, weight in graph[u]:
            newDistance = distance + weight
            if newDistance < dist[v]:
                dist[v] = newDistance
                prev[v] = u
                heapq.heappush(pq, (newDistance, v))
    return dist, prev

def build_graph(edges, directed=True):
    graph = {}
    for u, v, weight in edges:
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, [])
        if not directed:
            graph.setdefault(v, []).append((u, weight))
    return graph

def get_path(prev, start, target):
    if target not in prev:
        return None
    path, cur = [], target
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]
    else:
        return None
    return path[::-1]

if __name__ == '__main__':
    graph = build_graph(EDGES)
    dist, prev = dijkstra(graph, START)
    path = get_path(prev, START, TARGET)

    print("Minimal path:")
    for v in sorted(dist):
        print(f"  {v}: {dist[v]}")

    print(f"\nPath {START} -> {TARGET}: {path}")
    print(f"Length: {dist[TARGET]}")
