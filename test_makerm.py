#テストケースの作成(辺の重みは負を含む)
from random import sample,randint
n=1024
edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
for i in range(10):
    path=f"m{i}.txt"
    seedge=sample(edges,n*(2**i))
    with open(path,mode="w") as f:
        f.write(f"{n} {n*(2**i)}\n")
        for e in seedge:
            f.write(f"{e[0]} {e[1]} {randint(-n,n)}\n")