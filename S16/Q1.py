def tower_of_hanoi(n, source, target, auxiliary):
    """
    Function to solve the Tower of Hanoi problem using recursion.
    
    Parameters:
    n (int): Number of disks
    source (str): The source rod
    target (str): The target rod
    auxiliary (str): The auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, so they are out of the way
    tower_of_hanoi(n-1, source, auxiliary, target)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move the n-1 disks that we moved to auxiliary to the target rod
    tower_of_hanoi(n-1, auxiliary, target, source)

# Input the number of disks
n = int(input("Enter the number of disks: "))

# Call the tower_of_hanoi function to solve the puzzle
tower_of_hanoi(n, 'A', 'C', 'B')  # 'A' is source, 'C' is target, 'B' is auxiliary
