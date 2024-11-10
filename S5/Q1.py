def mean_end_analysis(S1, S2):
    """
    Perform a Mean-End Analysis to transform string S1 to string S2.
    
    :param S1: Initial string
    :param S2: Goal string
    :return: Sequence of steps to transform S1 to S2
    """
    steps = []
    
    while S1 != S2:
        # Find the positions where S1 and S2 differ
        diff = [(i, S1[i], S2[i]) for i in range(len(S1)) if S1[i] != S2[i]]
        
        # Choose the first mismatch and change it in S1
        if diff:
            index, current_char, goal_char = diff[0]
            S1 = S1[:index] + goal_char + S1[index + 1:]
            steps.append(f"Change {current_char} at index {index} to {goal_char}")
    
    return steps

# Example usage:
S1 = "abcdef"
S2 = "azcdef"
steps = mean_end_analysis(S1, S2)

print("Steps to transform S1 to S2:")
for step in steps:
    print(step)
