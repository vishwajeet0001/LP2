INF = 9999999
V = 5
cost=0

G = [
    [0, 4, 1, 2, 0],
    [4, 0, 0, 10, 0],                               
    [1, 0, 0, 6, 0],
    [2, 10, 6, 0, 3],
    [0, 0, 0, 3, 0]
]

dist = [INF] * V
visited = [False] * V

# Source vertex is assumed to be 0
source = 0
dist[source] = 0

for _ in range(V - 1):
    # Find vertex with the minimum distance
    min = INF
    x = -1                #index
    for i in range(V):
        if not visited[i] and dist[i] < min:
            min = dist[i]
            x = i
    
    # Mark the selected vertex as visited
    visited[x] = True
    
    # Update distances of adjacent vertices
    for i in range(V):
        if not visited[i] and G[x][i] and dist[x] + G[x][i] < dist[i]:
            dist[i] = dist[x] + G[x][i]
            cost=cost+dist[i]
        


# Print the minimum distances
print("Vertex   Distance from Source")
for i in range(V):
    print(f"{i}\t   {dist[i]}")

print("cost:",cost)
