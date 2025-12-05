from models.generative_ai import GenerativeAI

class GenerativeAIController:
    def __init__(self):
        'Controller class for GenerativeAI'
        self.__demo = GenerativeAI()

    def get_generated_text(self, prompt, temperature):
        return self.__demo.generate_text(prompt,\
                                         temperature=temperature,\
                                         max_tokens=50)