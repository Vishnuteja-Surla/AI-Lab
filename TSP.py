from itertools import permutations

Vertices = 5

def Travelling_Salesman(graph,start):
    perm_list = []
    for i in range(Vertices):
        if i!=start:
            perm_list.append(i)
    
    all_paths = permutations(perm_list)
        
    cost = []
    
    for i in all_paths:
        weight = 0
        k = start
        for j in i:
            weight += graph[k][j]
            k = j
        weight += graph[k][start]
        cost.append(weight)
    
    mincost = cost[0]
    minpos = 0
    for i in range(len(cost)):
        if cost[i] < mincost:
            mincost = cost[i]
            minpos = i
    iterator = 0        
    
    all_paths = permutations(perm_list)
    
    for i in all_paths:
        if minpos == iterator:
            print("Path = ",start,i,start)
            break
        iterator += 1
            
    print("Min Cost = ",mincost)

if __name__=="__main__":
    graph=[[0,12,10,19,8],[12,0,3,7,6],[10,3,0,2,20],[19,7,2,0,4],[8,6,20,4,0]]
    Travelling_Salesman(graph, 0)