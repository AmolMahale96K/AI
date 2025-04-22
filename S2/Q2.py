# Graph representation using adjacency matrix
graph = [
    [0, 1, 1, 0, 0, 0, 0],  # Node 1
    [1, 0, 0, 1, 1, 0, 0],  # Node 2
    [1, 0, 0, 0, 0, 1, 0],  # Node 3
    [0, 1, 0, 0, 0, 0, 0],  # Node 4
    [0, 1, 0, 0, 0, 1, 0],  # Node 5
    [0, 0, 1, 0, 1, 0, 0],  # Node 6
    [0, 0, 0, 0, 0, 0, 0]   # Node 7 (Goal node)
]

visited = [False] * len(graph)
goal_node = 6  # Index of Node 7 (goal node)
found = False  # To stop search after goal is found

def dfs(node):
    global found
    if found:
        return
    print(f"Visited Node: {node + 1}")
    visited[node] = True
    if node == goal_node:
        print("Goal node reached!")
        found = True
        return
    for i in range(len(graph)):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)

def main():
    print("DFS Traversal from Node 1 to Goal Node 7:")
    dfs(0)  # Node 1 corresponds to index 0

main()
