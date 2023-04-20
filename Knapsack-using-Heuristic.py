def find_heuristic(p_w, visited, weights, max_weight, values, w_in_bag, vertices):
    
    hue = 0
            
    dict(sorted(p_w.items(), key=lambda item: item[1]))
    
    for i in p_w:
        if w_in_bag + weights[i] <= max_weight:
            hue = hue + values[i]
            w_in_bag = w_in_bag + weights[i]
            
    return hue
        

def Knapsack(weights, values, max_weight, n, vertices):
    
    p_w = {}
    visited = []
    for i in range(n):
        p_w[vertices[i]] = values[vertices[i]]/weights[vertices[i]]
    #req_node = [path, weight, value, heuristic+value]
    req_node = [[],0,0,13000]
    
    
    for i in vertices:
        
        visited.append(i)
        
        f2 = find_heuristic(p_w, visited, weights, max_weight, values, req_node[-1][1], vertices)+req_node[-1][2]
        
        node2 = [req_node[-1][0], req_node[-1][1], req_node[-1][2], f2]
        
        if req_node[-1][1]+weight[i] < max_weight:
            
            f1 = find_heuristic(p_w, visited, weights, max_weight, values, req_node[-1][1]+weight[i], vertices)+req_node[-1][2]+value[i]
            
            node1 = [req_node[-1][0].append(i), req_node[-1][1]+weight[i], req_node[-1][2]+value[i], f1]
        
        else:
            node1 = node2
            
        if node1[-1] > node2[-1]:
            req_node.append(node1)
        else:
            req_node.append(node2)
            
    print(req_node[-1])
        

if __name__=="__main__":
    
    # n = int(input("Enter the number of objects : "))
    # obj_weights = []
    # obj_value = []
    # for i in range(n):
    #     weight = int(input(f"Enter weight of object-{i+1} : "))
    #     value = int(input(f"Enter value of object-{i+1} : "))
    #     obj_weight.append(weight)
    #     obj_value.append(value)
    # max_weight = int(input("Enter the weight limit of the Bag : "))
    vertices = ['A','B','C','D','E']
    obj_weights = {'A':10, 'B':100, 'C':300, 'D':1, 'E':200}
    obj_values = {'A':1000, 'B':2000, 'C':4000, 'D':5000, 'E':5000}
    max_weight = 400
    n = len(obj_weights)
    Knapsack(obj_weights, obj_values, max_weight, n, vertices)