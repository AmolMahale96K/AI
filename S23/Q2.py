# Depth First Search (DFS) implementation

def dfs(graph, start, goal):
    """
    Perform DFS to find a path from start node to goal node.
    :param graph: Graph represented as an adjacency list
    :param start: Starting node
    :param goal: Goal node
    """
    visited = set()  # To keep track of visited nodes
    path = []  # To store the path to the goal node

    # Helper function to perform DFS recursively
    def dfs_recursive(node):
        # Add the current node to the path and mark as visited
        visited.add(node)
        path.append(node)

        # If goal is found, return True
        if node == goal:
            return True

        # Visit all the unvisited neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_recursive(neighbor):
                    return True

        # Backtrack: remove the node from the path if the goal is not found
        path.pop()
        return False

    # Start DFS from the start node
    if dfs_recursive(start):
        print(f"Path from {start} to {goal}: {path}")
    else:
        print(f"No path found from {start} to {goal}")

# Graph representation as an adjacency list
graph = {
    1: [2],
    2: [1, 3, 5],
    3: [2, 4],
    4: [3, 7],
    5: [2, 6],
    6: [5, 7],
    7: [4, 6]
}

# Initial node = 2, Goal node = 7
dfs(graph, 2, 7)
