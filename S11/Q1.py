def means_end_analysis(start_str, goal_str):
    # Define the operations needed to transform one string into another
    def find_operations(current, target):
        operations = []
        if len(current) < len(target):
            operations.append("insert")
        elif len(current) > len(target):
            operations.append("delete")
        else:
            operations.append("substitute")
        return operations
    
    # Initial state (start string) and goal state (goal string)
    current = start_str
    goal = goal_str
    steps = []

    # Main loop for means-end analysis
    while current != goal:
        print(f"Current string: {current} | Goal string: {goal}")
        
        # Find the operations that will reduce the difference
        operations = find_operations(current, goal)
        
        # Choose the first operation and apply it
        if "insert" in operations:
            # Insert character at the end
            current += goal[len(current)]
            steps.append(f"Insert {goal[len(current)-1]} to form {current}")
        
        elif "delete" in operations:
            # Delete the last character
            current = current[:-1]
            steps.append(f"Delete {current[-1]} to form {current}")
        
        elif "substitute" in operations:
            # Substitute the last character
            current = current[:-1] + goal[len(current)-1]
            steps.append(f"Substitute {current[-1]} to form {current}")

    return steps

# Example usage
start_str = input("Enter start string: ")
goal_str = input("Enter goal string: ")

steps = means_end_analysis(start_str, goal_str)

print("\nTransformation steps:")
for step in steps:
    print(step)
