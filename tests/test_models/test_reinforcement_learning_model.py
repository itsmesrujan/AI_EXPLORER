# Reinforcement Learning Model Tests
def test_reinforcement_learning_initialization(reinforcement_learning_model):
    assert reinforcement_learning_model is not None
    assert hasattr(reinforcement_learning_model, 'train')
    assert hasattr(reinforcement_learning_model, 'optimal_path')

def test_reinforcement_learning_training(reinforcement_learning_model):
    q_table = reinforcement_learning_model.train()
    assert q_table is not None
    assert q_table.shape == (reinforcement_learning_model.grid_size,
                             reinforcement_learning_model.grid_size,
                             len(reinforcement_learning_model.actions))

def test_reinforcement_learning_optimal_path(reinforcement_learning_model):
    # Note that we are not validating q_table as it is covered as part of
    # separate function
    q_table = reinforcement_learning_model.train()
    path = reinforcement_learning_model.optimal_path()
    assert isinstance(path, list)
    assert len(path) > 0
    assert path[0] == reinforcement_learning_model.start
    assert path[-1] == reinforcement_learning_model.goal