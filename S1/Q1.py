import random

def hill_climbing(f, x_start, step_size=0.1, max_iter=100):
    current_x = x_start
    current_f = f(current_x)
    
    for _ in range(max_iter):
        next_x = current_x + step_size
        next_f = f(next_x)
        
        if next_f > current_f:
            current_x, current_f = next_x, next_f
        else:
            break  # Stop if we reach a peak
            
    return current_x, current_f

# Define the function
def f(x):
    return -x**2 + 4*x

# Starting point
x_start = random.uniform(0, 5)
result_x, result_f = hill_climbing(f, x_start)

print(f"Maximum at x = {result_x}, f(x) = {result_f}")
