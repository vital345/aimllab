def heuristic(node):
    return H_dist[node]

def change_heuristic(node, cost):
    H_dist[node] = cost
    return

def print_path(node):
    print(optimal_child_group[node], end="")
    node = optimal_child_group[node]
    if len(node) > 1:
        if node[0] in optimal_child_group:
            print("->", end="")
            print_path(node[0])
        if node[1] in optimal_child_group:
            print('->', end="")
            print_path(node[1])
    else:
        if node in optimal_child_group:
            print('->', end='')
            print_path(node)
    return

H_dist = { 
    'A': -1,
    'B': 4, 
    'C': 2, 
    'D': 3, 
    'E': 6,
    'F': 8, 
    'G': 2,
    'H': 0,
    'I': 0, 
    'J': 0
} 

all_node = { 
      'A': {'OR': ['B'], 'AND': [('C', 'D')]},
      'B': {'OR': ['E', 'F']}, 
      'C': {'OR': ['G'], 'AND': [('H', 'I')]}, 
      'D': {'OR': ['J']}
} 

def least_cost_group(and_node, or_node, marked={}):
    node_wise_cost = {}
    for node_pair in and_node:
        if node_pair[0] + node_pair[1] not in marked:
            cost = 0
            cost += heuristic(node_pair[0]] + node_pair[1]) + 2
            node_wise_cost[node_pair[0] + node_pair[1]]  = cost
    for node in or_node:
        if node not in marked:
            cost = 0
            cost += heuristic(node) + 1
            node_wise_cost[node] = cost
    min_cost = 9999999
    min_cost_group = None
    
    for key, value in node_wise_cost.items():
        if value < min_cost:
            min_cost = value
            min_cost_group = key
    return min_cost, min_cost_group

def aostar(n):
    and_node = []
    or_node = []
    
    if n in all_node:
        if 'AND' in all_node[n]:
            and_node = all_node[n]['AND']
        if 'OR' in all_node[n]:
            or_node = all_node[n]['OR']
            
    if len(or_node) == 0 and len(or_node) == 0:
        return
    
    solvable = False
    marked = {}
    
    while not solvable:
        if len(marked) == len(and_node) + len(or_node):
            solvable = True
            min_cost_least, min_cost_least_group = least_cost_group(and_node, or_node, {})
            change_heuristic(n, min_cost_least)
            optimal_child_group[n] = min_cost_least_group
            continue
        min_cost, min_cost_group = least_cost_group(and_node, or_node, marked)
        is_expanded = False
        
        if len(min_cost_group) > 1:
            if min_cost_group[0] in all_node:
                is_expanded = True
                aostar(min_cost_group[0])
            if min_cost_group[1] in all_node:
                is_expanded = True
                aostar(min_cost_group[1])
        else:
            if min_cost_group in all_node:
                is_expanded = True
                aostar(min_cost_group)
        
        if is_expanded:
            min_cost_verify, min_cost_group_verify = least_cost_group(and_node, or_node, {})
            if min_cost_group == min_cost_group_verify:
                solvable = True
                change_heuristic(n, min_cost_verify)
                optimal_child_group[n] = min_cost_group_verify
            else:
                change_heuristic(n, min_cost)
                optimal_child_group[n] = min_cost_group
                solvable = True
                
        marked[min_cost_group] = 1
    return heuristic(n)

optimal_child_group = {}
optimal_cost = aostar('A')
pprint('Nodes which gives optimal cost are') 
print_path('A') 
print('\nOptimal Cost is :: ', optimal_cost)
print('H_dist', H_dist)
