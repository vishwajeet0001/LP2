# BFS
graph = {0: [1, 2, 3],
         1: [4, 5],
         2: [6],
         3: [7],
         4: [],
         5: [],
         6: []
         }

visited = []

def bfs_recursive(visited, graph, queue, goal_node):
    if not queue:
        return
    m = queue.pop(0)
    print(m)
    if m == goal_node:
        print("Node is Found !!! ")
        return
    else:
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    bfs_recursive(visited, graph, queue, goal_node)

def bfs(visited, graph, start_node, goal_node):
    visited.append(start_node)
    queue = [start_node]
    print("The BFS Traversal is : ")
    bfs_recursive(visited, graph, queue, goal_node)

bfs(visited, graph, 0, 7)

#DFS
graph = {0: [1, 2, 3],
         1: [4, 5],
         2: [6],
         3: [7],
         4: [],
         5: [],
         6: []
         }

visited = []

def dfs(graph, node, goal):
    print("Node: ", node)
    visited.append(node)
    if node == goal:
        print("Goal node found!")
        return True
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal):
                return True
    return False

print("DFS traversal is:")
dfs(graph, 0, 7)
