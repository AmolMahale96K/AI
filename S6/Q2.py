from collections import deque

def bfs(graph, start, goal):
    """
    Perform Breadth First Search (BFS) on the graph from the start node to the goal node.
    
    :param graph: Dictionary representing the graph as an adjacency list
    :param start: The starting node
    :param goal: The target node we are trying to reach
    :return: List representing the path from start to goal if found, else None
    """
    # Initialize the queue with the start node and the path taken to reach that node
    queue = deque([(start, [start])])
    
    # Set to keep track of visited nodes to avoid cycles
    visited = set()
    visited.add(start)
    
    while queue:
        current_node, path = queue.popleft()
        
        # If we reached the goal node, return the path
        if current_node == goal:
            return path
        
        # Visit all neighbors of the current node
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # If no path is found, return None
    return None

# Example graph (adjacency list representation)
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 7],
    6: [3],
    7: [5, 8],
    8: [7]
}

# Start BFS from node 1 and search for node 8
start_node = 1
goal_node = 8
path = bfs(graph, start_node, goal_node)

if path:
    print(f"Path from node {start_node} to node {goal_node}: {path}")
else:
    print(f"No path found from node {start_node} to node {goal_node}")
