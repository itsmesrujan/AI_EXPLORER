from models.reinforcement_learning import ReinforcementLearning

class ReinforcementLearningController:
    def __init__(self):
        'Controller class for Reinforcement Learning'
        self.__reinforcementLearning_instance = ReinforcementLearning()

    def _get_learning_data(self):
        from matplotlib import colors
        self.__reinforcementLearning_instance.train()
        path = self.__reinforcementLearning_instance.optimal_path()
        grid = [[0] * self.__reinforcementLearning_instance.grid_size for _ in range(self.__reinforcementLearning_instance.grid_size)]
        # mark goal
        gx, gy = self.__reinforcementLearning_instance.goal
        grid[gx][gy] = 2
        # mark obstacles
        for ox, oy in self.__reinforcementLearning_instance.obstacles:
            grid[ox][oy] = -1
        # mark path
        for i, (px, py) in enumerate(path):
            grid[px][py] = 1
        cmap = colors.ListedColormap(['white', 'yellow', 'green', 'red'])
        bounds = [-1.5, -0.5, 0.5, 1.5, 2.5]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        return grid, cmap, norm