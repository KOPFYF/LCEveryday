'''
Dijkstra algorithm does not work with graphs having negative weight edges. 
The below image is a classic example of Dijsktra algorithm being unsuccessful with negative weight edges.

Dijkstra follows a simple rule if all edges have non negative weights, 
adding an edge will never make the path smaller. 
That's why it follows the greedy strategy and picks up the shortest path and in turn which turns out optimal.


Bellman-Ford solves this problem or reports there is a negative-weight cycle
'''


from collections import defaultdict
from heapq import *

def dijkstra(edges, source, target):
    # build ajacent list graph
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w

    # minheap stores (current cost, current node, current path)
    # mins(a hashmap) stores the shortest paths to all the other nodes
    hq, seen, dist = [(0, source, [source])], set(), {source: 0}
    while hq:
        cost, u, path = heappop(hq)
        if u == target:
            return cost, path
        for v, w in graph[u].items():
            if v not in dist or dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(hq, (dist[u] + w, v, path + [v]))
    print(hq)
    return -1, []


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
        ("F", "G", 11),
        ("H", "I", 100)
    ]

print("=== Dijkstra ===")
print(edges)
print("A -> E:")
print(dijkstra(edges, "A", "E"))
print("F -> G:")
print(dijkstra(edges, "F", "G"))
print("A -> I:")
print(dijkstra(edges, "A", "I"))