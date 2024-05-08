inf = 999999
V = 5  # Number of vertices
ne = 1  # Number of edges added
mincost = 0  # Total cost of minimum spanning tree
p = [0] * 9  # Parent array for disjoint set
cost=[
    [0,4,1,2,0],
    [4,0,0,10,0],
    [1,0,0,6,0],
    [2,10,6,0,3],
    [0,0,0,3,0]
] # Cost matrix of the graph

# Function to find the parent of a vertex in a disjoint set
def applyfind(i):
    while p[i] != 0:
        i = p[i]
    return i

# Function to perform union of two sets
def applyunion(i, j):
    if i != j:
        p[j] = i
        return 1
    return 0

# Replace zero weights with infinity
for i in range(V):
    for j in range(V):
        if cost[i][j] == 0:
            cost[i][j] = inf

print("Minimum Cost Spanning Tree:")
while ne < V:
    min_val = inf
    for i in range(V):
        for j in range(V):
            if cost[i][j] < min_val:
                min_val = cost[i][j]
                a = u = i
                b = v = j
    u = applyfind(u)
    v = applyfind(v)
    if applyunion(u, v) != 0:
        print(f"{a} -> {b}")
        mincost += min_val
    cost[a][b] = cost[b][a] = 999     #to mark it visited we write this part
    ne += 1

print(f"Minimum cost = {mincost}")
