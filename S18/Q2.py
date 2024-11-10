def depth_limited_dfs(graph, start, goal, depth_limit):
    """
    Perform Depth Limited DFS to find the goal node within the depth limit.
    """
    if start == goal:
        return [start]  # Return the path if the start is the goal

    if depth_limit == 0:
        return None  # Return None if we reach the depth limit

    for neighbor in graph[start]:
        # Explore the neighbor recursively
        path = depth_limited_dfs(graph, neighbor, goal, depth_limit - 1)
        if path:
            return [start] + path  # Return the path if found

    return None  # Return None if no path found

def iterative_deepening_dfs(graph, start, goal):
    """
    Perform Iterative Deepening DFS to find the goal node.
    """
    depth_limit = 0
    while True:
        print(f"Searching at depth limit {depth_limit}")
        path = depth_limited_dfs(graph, start, goal, depth_limit)
        if path:
            return path  # Return the path if goal is found
        depth_limit += 1  # Increase depth limit if goal is not found

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Perform Iterative Deepening DFS from 'A' to 'G'
start_node = 'A'
goal_node = 'G'
path = iterative_deepening_dfs(graph, start_node, goal_node)

if path:
    print(f"Path to goal {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found to {goal_node}")
