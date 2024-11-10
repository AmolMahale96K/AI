import heapq

class Node:
    def __init__(self, name, g, h):
        self.name = name  # Node name
        self.g = g  # Cost from start node to this node
        self.h = h  # Heuristic estimate of the cost to the goal
        self.f = g + h  # f = g + h, total cost (actual + heuristic)
        self.parent = None  # To track the path

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal, heuristic):
    # Create a priority queue (min-heap) to store nodes to explore
    open_list = []
    closed_list = set()

    # Initialize the start node
    start_node = Node(start, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)

        # If we reached the goal, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (from start to goal)

        closed_list.add(current_node.name)

        # Explore neighbors
        for neighbor, weight in graph[current_node.name]:
            if neighbor in closed_list:
                continue

            g = current_node.g + weight
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, g, h)
            neighbor_node.parent = current_node

            # If the neighbor is not in the open list or found a better path, add it
            if not any(node.name == neighbor and node.f <= neighbor_node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # If no path is found

# Example graph as adjacency list (nodes and edge weights)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic values (straight-line distance to goal node 'D')
heuristic = {
    'A': 7,  # Estimated cost from 'A' to 'D'
    'B': 6,  # Estimated cost from 'B' to 'D'
    'C': 2,  # Estimated cost from 'C' to 'D'
    'D': 0   # Goal node, heuristic is 0
}

# Run the A* algorithm from 'A' to 'D'
start = 'A'
goal = 'D'
path = a_star(graph, start, goal, heuristic)

print(f"Path from {start} to {goal}: {path}")
