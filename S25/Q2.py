from collections import deque

# Define the goal state
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Directions for sliding the tiles (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row, col) offsets for up, down, left, right

def is_valid_move(state, row, col):
    """Check if the move is within bounds."""
    return 0 <= row < 3 and 0 <= col < 3

def get_neighbors(state):
    """Generate all possible states by sliding the empty space."""
    neighbors = []
    # Find the position of the empty space (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
                break

    # Try to move in each direction
    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if is_valid_move(state, new_row, new_col):
            # Swap the empty space with the adjacent tile
            new_state = list(list(row) for row in state)  # Deep copy
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(tuple(tuple(row) for row in new_state))  # Convert back to tuple for immutability
    return neighbors

def bfs(start_state):
    """Breadth First Search to solve the 8-puzzle."""
    queue = deque([(start_state, [])])  # Store (state, path to reach the state)
    visited = set([start_state])  # To track visited states

    while queue:
        current_state, path = queue.popleft()

        # If the goal state is reached, return the path
        if current_state == goal_state:
            return path

        # Generate neighbors and add to the queue
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No solution found

# Example usage
start_state = ((1, 2, 3), (4, 5, 6), (0, 7, 8))  # Initial state (example)
solution = bfs(start_state)

if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
else:
    print("No solution found")
