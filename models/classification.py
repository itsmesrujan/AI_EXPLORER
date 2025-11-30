from sklearn.datasets import make_classification

class Classification:
    def __init__(self):
        'model class for classification'
        pass

    def get_classification_data(\
            self,\
            n_samples=200,\
            n_features=2,\
            n_redundant=0,\
            n_clusters_per_class=1,\
            random_state=42):
        x, y = make_classification(
            n_samples=n_samples,
            n_features=n_features,
            n_redundant=n_redundant,
            n_clusters_per_class=n_clusters_per_class,
            random_state=random_state
        )
        return x, y