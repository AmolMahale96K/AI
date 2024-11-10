def f(x):
    """
    The objective function f(x) = -x^2 + 4x.
    """
    return -x**2 + 4*x

def hill_climbing(starting_point, step_size, max_iterations):
    """
    Hill climbing algorithm to find the maximum of a function.
    :param starting_point: The starting point for the search
    :param step_size: The step size for moving to a neighboring solution
    :param max_iterations: Maximum number of iterations
    :return: The best solution found and its value
    """
    current_point = starting_point
    current_value = f(current_point)

    for _ in range(max_iterations):
        # Generate neighbors by moving in the positive and negative direction
        neighbor1 = current_point + step_size
        neighbor2 = current_point - step_size

        # Calculate the value of the objective function at the neighbors
        value1 = f(neighbor1)
        value2 = f(neighbor2)

        # Compare the neighbor values to decide the direction to move
        if value1 > current_value:
            current_point = neighbor1
            current_value = value1
        elif value2 > current_value:
            current_point = neighbor2
            current_value = value2
        else:
            # If neither neighbor is better, we stop the search (local maximum)
            break

    return current_point, current_value

# Example usage
starting_point = 0  # Initial point for the search
step_size = 0.1  # Step size for moving to neighbors
max_iterations = 100  # Maximum number of iterations

best_x, best_value = hill_climbing(starting_point, step_size, max_iterations)
print(f"Best x found: {best_x}")
print(f"Maximum value of f(x) = {best_value}")
