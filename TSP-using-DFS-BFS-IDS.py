from collections import deque
from typing import List
import sys

INF = sys.maxsize

def solve_TSP_DFS(graph):
    n = len(graph)
    return DFS_TSP(graph, 0, [0], n, 0)

def DFS_TSP(graph, vertex, visited, n, cost):
    if len(visited) == n:
        return cost + graph[vertex][0]
        
    min_cost = INF
    
    for v in range(n):
        if v not in visited:
            new_cost = DFS_TSP(graph, v, visited + [v], n ,cost + graph[vertex][v])
            min_cost = min(min_cost, new_cost)
            
    return min_cost
    
def solve_TSP_BFS(graph):
    n = len(graph)
    return BFS_TSP(graph, n)
    
def BFS_TSP(graph, n):
    q = deque([(0,0,[0])])
    
    while q:
        (cost, vertex, visited) = q.popleft()
        if len(visited) == n:
            return cost + graph[vertex][0]
        for v in range(n):
            if v not in visited:
                q.append((cost+graph[vertex][v], v, visited + [v]))
                
    return INF
            
def solve_TSP_IDS(graph):
    n = len(graph)
    limit = 0
    for u in range(n):
        for v in range(n):
            limit = max(limit, graph[u][v])
            
    limit *= n
    while limit >= 0:
        res = IDS_TSP(graph, 0 ,1, 0, limit)
        if res != INF:
            print(f"Minimum Cost for the path using IDS is : {res}")
            return
        limit = int(limit/2)

def IDS_TSP(graph, u, mask, d, limit):
    n = len(graph)
    if d + graph[u][0] > limit:
        return INF
    if mask == (1<<n)-1:
        return d + graph[u][0]
    res = INF
    for v in range(n):
        if mask & (1<<v) == 0:
            res = min(res, IDS_TSP(graph, v, mask | (1<<v), d+graph[u][v], limit))
    return res

if __name__ == "__main__":
    
    vertices = [0,1,2,3,4]
    
    graph = [[0,12,10,19,8],[12,0,3,7,6],[10,3,0,2,20],[19,7,2,0,4],[8,6,20,4,0]]
    
    print(f"Minimum Cost for the path using DFS is : {solve_TSP_DFS(graph)}")
    print(f"Minimum Cost for the path using BFS is : {solve_TSP_BFS(graph)}")
    solve_TSP_IDS(graph)