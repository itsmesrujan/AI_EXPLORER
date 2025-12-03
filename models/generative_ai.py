from transformers import GPT2LMHeadModel, GPT2Tokenizer
# [TODO] Use AutoModel and AutoTokenizer to support multiple models
# from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GenerativeAI:
    def __init__(self, model_id="gpt2"):
        'model class for generative AI using GPT-2'
        print("Loading model...")
        # As its a common practice, we define special tokens
        SPECIAL_TOKENS = {'pad_token': '<PAD>',
                          'bos_token': '<BOS>',
                          'eos_token': '<EOS>',
                          'unk_token': '<UNK>'}
        self.__tokenizer = GPT2Tokenizer.from_pretrained(model_id)
        # add new special tokens to the tokenizer
        self.__tokenizer.add_special_tokens(SPECIAL_TOKENS)
        self.__model = GPT2LMHeadModel.from_pretrained(model_id)
        self.__model.resize_token_embeddings(len(self.__tokenizer))
        self.__model.eval()  # inference mode
        # Model configurations for generation can be set here if needed
        self.__model.config.pad_token_id = self.__tokenizer.pad_token_id
        self.__model.config.eos_token_id = self.__tokenizer.eos_token_id

    def generate_text(self, prompt, temperature=0.7, max_tokens=100):
        try:
            if prompt!='':
                inputs = self.__tokenizer.encode(prompt, return_tensors="pt")
                outputs = self.__model.generate(
                    inputs,
                    max_length=max_tokens,
                    temperature=temperature,
                    top_p=0.9,
                    do_sample=True,
                    pad_token_id=self.__tokenizer.eos_token_id
                )
                return self.__tokenizer.decode(outputs[0], skip_special_tokens=True)
            else:
                return "Please provide a valid prompt."
        except Exception as e:
            print(f"Error during text generation: {e}")
            return "Error generating text."