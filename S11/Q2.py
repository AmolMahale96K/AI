from collections import deque

# Function to perform BFS and find the solution
def water_jug_bfs(capacity1, capacity2, target):
    # The initial state (both jugs are empty)
    initial_state = (0, 0)  # (amount in jug1, amount in jug2)
    
    # Queue for BFS (stores the state and the path to get there)
    queue = deque([(initial_state, [])])
    
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    
    # Define the possible operations
    def get_neighbors(state):
        jug1, jug2 = state
        neighbors = []
        
        # Fill jug1 (4 gallons)
        neighbors.append((capacity1, jug2))
        
        # Fill jug2 (3 gallons)
        neighbors.append((jug1, capacity2))
        
        # Empty jug1
        neighbors.append((0, jug2))
        
        # Empty jug2
        neighbors.append((jug1, 0))
        
        # Pour water from jug1 to jug2
        pour_to_jug2 = min(jug1, capacity2 - jug2)
        neighbors.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        
        # Pour water from jug2 to jug1
        pour_to_jug1 = min(jug2, capacity1 - jug1)
        neighbors.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
        
        return neighbors
    
    # Perform BFS to find the solution
    while queue:
        current_state, path = queue.popleft()
        jug1, jug2 = current_state
        
        # If we reached the target state (target gallons in jug2)
        if jug2 == target:
            return path + [current_state]
        
        # Explore the neighbors (possible operations)
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    
    return None  # No solution found

# Function to print the solution steps
def print_solution(solution):
    if solution:
        for step in solution:
            print(f"Jug1: {step[0]} gallons, Jug2: {step[1]} gallons")
    else:
        print("No solution found.")

# Example usage
capacity1 = 4  # Capacity of jug1 (4 gallons)
capacity2 = 3  # Capacity of jug2 (3 gallons)
target = 2  # Target quantity in jug2 (3-gallon jug)

solution = water_jug_bfs(capacity1, capacity2, target)
print_solution(solution)
