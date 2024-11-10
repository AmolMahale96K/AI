def hill_climbing(function, start, step_size, iterations):
    current = start
    current_value = function(current)

    for i in range(iterations):
        # Check neighboring points (current + step_size and current - step_size)
        neighbors = [current + step_size, current - step_size]
        
        # Evaluate the neighbors
        neighbor_values = [function(neighbor) for neighbor in neighbors]
        
        # Find the best neighbor
        best_value = max(neighbor_values)
        
        if best_value > current_value:
            # Move to the best neighbor
            current = neighbors[neighbor_values.index(best_value)]
            current_value = best_value
            print(f"Iteration {i+1}: Moving to x = {current}, f(x) = {current_value}")
        else:
            # If no improvement, stop
            print(f"Iteration {i+1}: No improvement, stopping at x = {current}, f(x) = {current_value}")
            break
            
    return current, current_value

# The function to be maximized
def function(x):
    return -x**2 + 4*x

# Parameters for the hill climbing algorithm
start = 0.0   # Starting point
step_size = 0.1  # Step size
iterations = 50  # Number of iterations

# Run hill climbing algorithm
optimal_x, optimal_value = hill_climbing(function, start, step_size, iterations)

print(f"Optimal solution found: x = {optimal_x}, f(x) = {optimal_value}")
