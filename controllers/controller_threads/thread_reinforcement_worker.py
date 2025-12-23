from PySide6.QtCore import Signal
from utils.threads.thread_base_worker import ThreadBaseWorker

class ThreadReinforcementWorker(ThreadBaseWorker):

    def __init__(self, model, delay=0.4):
        """
        A worker thread class for Reinforcement Learning
        """
        super().__init__()
        self.model = model
        self.delay = delay
        self.result = None

    def execute(self):
        try:
            from matplotlib import colors
            self.model.train()
            path = self.model.optimal_path()
            import numpy as np
            # create grid as numpy array
            grid = np.zeros((self.model.grid_size, self.model.grid_size), dtype=int)
            # mark goal
            gx, gy = self.model.goal
            grid[gx, gy] = 2
            # mark obstacles
            for ox, oy in self.model.obstacles:
                grid[ox, oy] = -1
            # mark path
            for i, (px, py) in enumerate(path):
                grid[px, py] = 1
            # Create color map and norm
            cmap = colors.ListedColormap(['white', 'yellow', 'green', 'red'])
            bounds = [-1.5, -0.5, 0.5, 1.5, 2.5]
            norm = colors.BoundaryNorm(bounds, cmap.N)
            self.result = (grid, cmap, norm)
        except Exception as e:
            print(f"Exception in thread: {e}")
            import traceback
            traceback.print_exc()
            self.error.emit(str(e))