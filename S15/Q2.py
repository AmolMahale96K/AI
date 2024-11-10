def dfs_with_depth_limit(graph, node, goal, depth_limit, visited):
    """Performs DFS with depth limit."""
    if node == goal:
        return [node]
    if depth_limit == 0:
        return None
    
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            path = dfs_with_depth_limit(graph, neighbor, goal, depth_limit - 1, visited)
            if path:
                return [node] + path
    return None

def iterative_deepening_dfs(graph, start, goal):
    """Performs Iterative Deepening DFS."""
    depth = 0
    while True:
        visited = set()
        path = dfs_with_depth_limit(graph, start, goal, depth, visited)
        if path:
            return path
        depth += 1

# Example graph representation (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Goal node
goal = 'G'
start = 'A'

# Run the IDDFS algorithm
path = iterative_deepening_dfs(graph, start, goal)
print(f"Path to goal {goal}: {path}")
