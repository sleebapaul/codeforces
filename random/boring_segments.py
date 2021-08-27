"""
1555E - From segment tree. Skipping as of now. 
"""

def inlt():
    """
    For taking List inputs.
    """
    return(list(map(int,input().split())))

def is_neighbor(node_a, node_b):
    if max(node_a[:2]) < max(node_b[:2]) and max(node_a[:2]) >= min(node_b[:2]):
        return True
    return False

def build_graph(arr):
    graph = {i:[] for i in range(len(arr))}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if is_neighbor(arr[i], arr[j]):
                    graph[i].append(j)
    return graph

def dfs(node_idx, graph, arr, dest, path, visited, result):
    if node_idx not in visited:
        path.append(node_idx)
        visited.add(node_idx)
    
    if arr[node_idx][1] == dest:
        result.append([arr[i][2] for i in path])
    else:
        for neighbour in graph[node_idx]:
            dfs(neighbour, graph, arr, dest, path, visited, result)
    
    visited.remove(node_idx)
    path.pop()


def problem(arr, n, m):

    graph = build_graph(arr)
    result = []
    dfs(0, graph, arr, m, [], set(), result)
    out = float("inf")
    for res in result:
        tmp = max(res) - min(res)
        out = min(out, tmp)
    print(out)
    

[n, m] = inlt()
arr = []
for _ in range(n):
    int_array = inlt()
    arr.append(int_array)

problem(arr, n, m)