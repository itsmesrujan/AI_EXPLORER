class ModelFactory:
    __registry = {}

    @classmethod
    def register_model(cls, model_name, model_class):
        cls.__registry[model_name] = model_class

    @classmethod
    def create_model(cls, model_name):
        try:
            return cls.__registry.get(model_name)
        except ValueError:
            raise ValueError(f"Model '{model_name}' is not registered in the factory.")