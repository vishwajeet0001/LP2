INF=9999999
V=5

G=[
    [0,4,1,2,0],
    [4,0,0,10,0],
    [1,0,0,6,0],
    [2,10,6,0,3],
    [0,0,0,3,0]
]

sel=[False]*5
n=0
sel[0]=True
cost=0

print("Edge:"+"weight")
while n<V-1:
    min=INF
    x=0
    y=0

    for i in range(V):
        if sel[i]:
            for j in range(V):
                if not sel[j] and G[i][j]:
                    if min>G[i][j]:
                        min=G[i][j]
                        x=i
                        y=j
    print(f"{x}-{y}:{G[x][y]}")
    sel[y]=True
    n+=1
    cost=G[x][y]+cost


print("total cost:",cost)