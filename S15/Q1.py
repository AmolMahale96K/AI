class MonkeyBananaProblem:
    def __init__(self):
        # Initial state: (monkey_position, box_position, banana_position)
        self.initial_state = (0, 0, 4)  # Monkey at position 0, box at position 0, bananas at position 4
        self.goal_state = (4, 0, 4)     # Goal is for the monkey to be at position 4 with the box at position 0

    def is_goal_state(self, state):
        return state == self.goal_state

    def actions(self, state):
        monkey_pos, box_pos, banana_pos = state
        actions = []
        
        # Action 1: Move monkey left or right
        if monkey_pos > 0:
            actions.append(('move_left', (monkey_pos - 1, box_pos, banana_pos)))
        if monkey_pos < 4:
            actions.append(('move_right', (monkey_pos + 1, box_pos, banana_pos)))

        # Action 2: Push the box
        if monkey_pos == box_pos:
            if box_pos > 0:
                actions.append(('push_left', (monkey_pos, box_pos - 1, banana_pos)))
            if box_pos < 4:
                actions.append(('push_right', (monkey_pos, box_pos + 1, banana_pos)))
        
        # Action 3: Jump to get the bananas if the box is underneath
        if monkey_pos == box_pos and box_pos == banana_pos:
            actions.append(('jump', (monkey_pos, box_pos, banana_pos)))
        
        return actions

    def search(self):
        # Use a simple DFS approach to find the solution
        stack = [self.initial_state]
        visited = set()

        while stack:
            state = stack.pop()
            if state in visited:
                continue
            visited.add(state)

            # Check if it's the goal state
            if self.is_goal_state(state):
                print(f"Goal Reached: Monkey at {state[0]}, Box at {state[1]}, Bananas at {state[2]}")
                return state

            # Explore the next actions
            for action, new_state in self.actions(state):
                if new_state not in visited:
                    print(f"Action: {action}, New State: {new_state}")
                    stack.append(new_state)

        print("No solution found.")
        return None

# Create an instance of the problem and search for the solution
problem = MonkeyBananaProblem()
problem.search()
