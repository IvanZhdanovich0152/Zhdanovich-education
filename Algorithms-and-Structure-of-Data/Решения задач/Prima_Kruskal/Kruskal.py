class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(edges, num_vertices):
    edges = sorted(edges, key=lambda e: e[2])
    dsu = DSU(num_vertices)

    mst = []
    total = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == num_vertices - 1:
                break

    return mst, total


edges2 = [
    (0, 1, 7), (0, 3, 5),
    (1, 2, 8), (1, 3, 9), (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15), (3, 5, 6),
    (4, 5, 8), (4, 6, 9),
    (5, 6, 11),
]

mst2, total2 = kruskal(edges2, 7)
print("MST edges:")
for u, v, w in mst2:
    print(f"  {u} -- {v} : {w}")
print(f"Total weight = {total2}")