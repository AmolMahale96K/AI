graph = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

visited = [False] * len(graph)

def dfs(node):
    print(node, end="\t")
    visited[node] = True
    for i in range(len(graph)):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)

def main():
    print("DFS Traversal starting from node 0:")
    dfs(0)

main()
