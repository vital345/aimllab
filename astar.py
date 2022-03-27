def heuristic(node):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0             
    }
    return H_dist[node]

Graph_node = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
     
}

def get_neighbors(node):
    if node in Graph_node:
        return Graph_node[node]
    else:
        return None

def astar(start, stop):
    open_ = set(start)
    close = set()
    parent = {start : start}
    g = {start: 0}
    
    while len(open_) > 0:
        n = None
        for v in open_:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop or Graph_node[n] == None:
            pass
        else:
            for m, weight in get_neighbors(n):
                if m not in open_ or m not in close:
                    g[m] = g[n] + weight
                    parent[m] = n
                    open_.add(m)
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                    if m in close:
                        close.remove(m)
                        open_.add(m)
        if n == None:
            print('Path not found')
            return
        
        if n == stop:
            path = []
            while n != parent[n]:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print(path)
            return
        close.add(n)
        open_.remove(n)
    print('Path not found')
    return

astar('A', 'J')
