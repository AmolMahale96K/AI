from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node == goal:
            print(f"Goal node {goal} found!")
            return True

        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
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
breadth_first_search(graph, start=1, goal=8)
