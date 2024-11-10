def depth_first_search(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        
        if node == goal:
            print(f"Goal node {goal} found!")
            return True
        
        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)
            
            # Add unvisited neighbors to stack in reverse order for correct DFS order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    print("Goal node not found.")
    return False

# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [7, 8],
    6: [],
    7: [],
    8: []
}

# Initial node is 1, Goal node is 8
depth_first_search(graph, start=1, goal=8)
