import matplotlib.pyplot as plt

class Common:
    def __init__(self):
        'common utilities for models and views'
        pass

    def get_plot_figure(self):
        try:
            return plt.figure()
        except Exception as e:
            print(f"Error while creating plot figure: {e}")
            return None