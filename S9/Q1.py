import heapq

# The goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define possible movements (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to calculate Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                target_x = (tile - 1) // 3
                target_y = (tile - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Function to find the position of the empty space (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to generate the possible moves from the current state
def generate_neighbors(state):
    neighbors = []
    blank_x, blank_y = find_blank(state)

    for dx, dy in moves:
        new_x, new_y = blank_x + dx, blank_y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            neighbors.append(new_state)
    return neighbors

# A* algorithm to solve the 8-puzzle
def a_star(start_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0 + manhattan_distance(start_state), 0, start_state, []))

    while open_list:
        _, g_cost, current_state, path = heapq.heappop(open_list)

        # If we reached the goal state
        if current_state == goal_state:
            return path + [current_state]

        closed_list.add(tuple(map(tuple, current_state)))

        for neighbor in generate_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in closed_list:
                f_cost = g_cost + 1 + manhattan_distance(neighbor)
                heapq.heappush(open_list, (f_cost, g_cost + 1, neighbor, path + [current_state]))

    return None  # No solution found

# Function to print the puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()

# Example usage
start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]  # Example starting state
solution = a_star(start_state)

if solution:
    print("Solution found:")
    for state in solution:
        print_state(state)
else:
    print("No solution found.")
