from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class GenerativeAIDemo:
    def __init__(self, model_name="gpt2"):
        print("Loading model...")
        # As its a common practice, we define special tokens
        SPECIAL_TOKENS = {'pad_token': '<PAD>',
                          'bos_token': '<BOS>',
                          'eos_token': '<EOS>',
                          'unk_token': '<UNK>'}
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        # add new special tokens to the tokenizer
        self.tokenizer.add_special_tokens(SPECIAL_TOKENS)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.resize_token_embeddings(len(self.tokenizer))
        self.model.eval()  # inference mode
        # Model configurations for generation can be set here if needed
        self.model.config.pad_token_id = self.tokenizer.pad_token_id
        self.model.config.eos_token_id = self.tokenizer.eos_token_id

    def generate_text(self, prompt, temperature=0.7, max_tokens=100):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=max_tokens,
            temperature=temperature,
            top_p=0.9,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)