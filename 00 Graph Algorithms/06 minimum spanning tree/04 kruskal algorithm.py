ipt = [[1,2,1], [1,3,3], [2,6,4], [3,4,1], [3,6,2], [4,5,5], [6,7,2], [6,5,6], [7,5,7]]

nodes = set()
for u,v,d in ipt:
    nodes.add(u)
    nodes.add(v)
n = len(nodes)

parent = {}
for node in nodes:
    parent[node] = node
rank = dict.fromkeys(parent, 1)

def findParent(node):
    if node == parent[node]:
        return node
    else:
        return findParent(parent[node])

def union(x,y, mst):
    xroot = findParent(x)
    yroot = findParent(y)
    if xroot == yroot:  # if both xroot and yroot are same, it means that they have same parent ie. they are already connected and if we still connect them, it will form a cycle
        pass
    else:
        mst.append([x,y])
        if rank[xroot] >= rank[yroot]:
            parent[yroot] = xroot
            rank[xroot] += rank[yroot]
        else:
            parent[xroot] = yroot
            rank[yroot] += rank[xroot]

mst = []
ipt = sorted(ipt, key=lambda x:x[2])
for u,v,d in ipt:
    union(u,v, mst)
for item in mst:
    print(item)


##########################################################################
# other way to put it # you can print distance too # clean code
##########################################################################

ipt = [[1,2,1], [1,3,3], [2,6,4], [3,4,1], [3,6,2], [4,5,5], [6,7,2], [6,5,6], [7,5,7]]

n = 7
parent = [v for v in range(n+1)]
rank = [1 for i in range(n+1)]

def findParent(node):
    if parent[node] == node:
        return node
    return findParent(parent[node])

def union(x, y):
    xroot = findParent(x)
    yroot = findParent(y)
    if xroot != yroot:
        if rank[xroot] >= rank[yroot]:
            parent[yroot] = xroot
            rank[xroot] += rank[yroot]
        else:
            parent[xroot] = yroot
            rank[yroot] += rank[xroot]
        return True     # true bcoz union happened
    return False    # false bcoz union didn't happen

ans = []
ipt = sorted(ipt, key=lambda x:x[2])
for u,v,d in ipt:
    if union(u,v):
        print(u,v, '-->', d)