from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    # build ajacent list graph
    graph = defaultdict(list)
    for u, v, edge in edges:
        graph[u].append((edge, v))

    # minheap stores (current cost, current node, current path)
    # mins(a hashmap) stores the shortest paths to all the other nodes
    minheap, seen, mins = [(0, f, ())], set(), {f: 0}
    while minheap:
        (cost, v1, path) = heappop(minheap)
        # given d[v1], find d[v2] using w[v1, v2]
        if v1 not in seen:
            # 因为MinHeap出来以后才做的结算, 进去时候是不能保证做结算的
            seen.add(v1) 
            path = (v1, path)
            if v1 == t: # get to the end node
                print('mins:', mins)
                return (cost, path)

            for weight, v2 in graph.get(v1, ()):
                # search neighbors and update 
                if v2 in seen: 
                    continue
                prev = mins.get(v2, None)
                # d[v2] = d[v1] + w[v1, v2]
                next_cost = cost + weight
                if prev is None or next_cost < prev:
                    mins[v2] = next_cost
                    heappush(minheap, (next_cost, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

print("=== Dijkstra ===")
print(edges)
print("A -> E:")
print(dijkstra(edges, "A", "E"))
print("F -> G:")
print(dijkstra(edges, "F", "G"))