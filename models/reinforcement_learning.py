import numpy as np

class ReinforcementLearning:
    def __init__(self, grid_size=5, episodes=200, alpha=0.1, gamma=0.9, epsilon=0.2):
        'model class for Reinforcement Learning using Q-Learning'
        self.grid_size = grid_size
        self.episodes = episodes
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = ['up', 'down', 'left', 'right']
        self.q_table = np.zeros((grid_size, grid_size, len(self.actions)))
        # Environment definition
        self.start = (0, 0)
        self.goal = (4, 4)
        self.obstacles = [(1, 3), (2, 2), (3, 1)]

    def _get_next_state(self, state, action):
        x, y = state
        if action == 'up':
            x = max(0, x - 1)
        elif action == 'down':
            x = min(self.grid_size - 1, x + 1)
        elif action == 'left':
            y = max(0, y - 1)
        elif action == 'right':
            y = min(self.grid_size - 1, y + 1)
        return (x, y)

    def _get_reward(self, state):
        if state == self.goal:
            return 10
        if state in self.obstacles:
            return -5
        return -0.1

    def _choose_action(self, state):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.actions)
        x, y = state
        return self.actions[np.argmax(self.q_table[x, y])]

    def train(self):
        for _ in range(self.episodes):
            state = self.start
            while state != self.goal:
                action = self._choose_action(state)
                next_state = self._get_next_state(state, action)
                reward = self._get_reward(next_state)
                x, y = state
                a = self.actions.index(action)
                # Q-learning update
                best_next = np.max(self.q_table[next_state[0], next_state[1]])
                self.q_table[x, y, a] += self.alpha * (reward + self.gamma * best_next - self.q_table[x, y, a])
                state = next_state
        return self.q_table

    def optimal_path(self):
        """Compute greedy path from start to goal for visualization."""
        state = self.start
        path = [state]
        visited = set()
        for _ in range(50):  # safety limit
            if state == self.goal:
                break
            visited.add(state)
            x, y = state
            action_idx = np.argmax(self.q_table[x, y])
            action = self.actions[action_idx]
            next_state = self._get_next_state(state, action)
            if next_state in visited:
                break # avoid loops
            path.append(next_state)
            state = next_state
        return path