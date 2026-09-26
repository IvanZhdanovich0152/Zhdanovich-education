EDGES = [
    (1, 2, 1),
    (1, 3, 1),
    (1, 4, 4),
    (2, 1, 6),
    (2, 4, 5),
    (3, 1, 1),
    (3, 4, 1),
    (4, 2, 5),
    (4, 3, 4),
]
NODES = [1, 2, 3, 4]


def floyd_warshall(nodes, edges):
    INF = float('inf')
    n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}

    dist = [[INF] * n for _ in range(n)]
    nxt = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        i, j = idx[u], idx[v]
        if w < dist[i][j]:
            dist[i][j] = w
            nxt[i][j] = v

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    return dist, nxt, idx


def reconstruct_path(nxt, idx, u, v):
    if nxt[idx[u]][idx[v]] is None:
        return None
    path = [u]
    cur = u
    while cur != v:
        cur = nxt[idx[cur]][idx[v]]
        if cur is None:
            return None
        path.append(cur)
    return path

if __name__ == '__main__':
    dist, nxt, idx = floyd_warshall(NODES, EDGES)

    print("Matrix shortest paths:")
    print("     " + "".join(f"{v:>6}" for v in NODES))
    for i, u in enumerate(NODES):
        row = "".join(
            f"{('inf' if dist[i][j] == float('inf') else dist[i][j]):>6}"
            for j in range(len(NODES))
        )
        print(f"{u:>4} {row}")

    print("\nAll shortest paths:")
    for u in NODES:
        for v in NODES:
            if u == v:
                continue
            p = reconstruct_path(nxt, idx, u, v)
            d = dist[idx[u]][idx[v]]
            d_str = 'inf' if d == float('inf') else d
            print(f"  {u} -> {v}: path {p}, distance {d_str}")

