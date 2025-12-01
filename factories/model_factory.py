# [TODO] Update this class to register new models as they are added
class ModelFactory:
    __registry = {}

    @classmethod
    def register_model(cls, model_name, model_class):
        cls.__registry[model_name] = model_class

    @classmethod
    def create_model(cls, model_name):
        model_class = cls.__registry.get(model_name)
        if model_class:
            return model_class()
        else:
            raise ValueError(f"Model '{model_name}' is not registered in the factory.")