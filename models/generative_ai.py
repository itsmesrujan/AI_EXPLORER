# from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class GenerativeAI:
    def __init__(self, model_id="gpt2"):
        'model class for generative AI using GPT-2 model'
        self._device = self._select_device()
        # Load tokenizer
        self._tokenizer = AutoTokenizer.from_pretrained(model_id)
        # GPT-2 has no pad token → use eos token
        if self._tokenizer.pad_token is None:
            self._tokenizer.pad_token = self._tokenizer.eos_token
        # Load model
        self._model = AutoModelForCausalLM.from_pretrained(model_id)
        self._model.to(self._device)
        self._model.eval()

    def _select_device(self):
        # CUDA available and actually works
        if torch.cuda.is_available():
            try:
                torch.cuda.current_device()
                return torch.device("cuda")
            except Exception:
                pass # CUDA is broken → fall back
        # Apple Silicon (M1/M2/M3)
        if torch.backends.mps.is_available() and torch.backends.mps.is_built():
            return torch.device("mps")
        # CPU fallback
        return torch.device("cpu")

    def get_input_tokens(self, prompt: str):
        """ Tokenize input prompt """
        try:
            inputs = self._tokenizer(prompt, return_tensors="pt").to(self._device)
            return inputs
        except Exception as e:
            print(f"Error during tokenization: {e}")
            return None

    def generate_text(self,\
                      prompt: str,\
                      max_new_tokens: int = 100,\
                      temperature: float = 0.7,\
                      top_p: float = 0.9,\
                      top_k: int = 40,\
                      repetition_penalty: float = 1.2) -> str:
        """ Generate text with safe defaults """
        if not prompt.strip():
            return "Error: Prompt cannot be empty."
        try:
            inputs = self.get_input_tokens(prompt)
            output_ids = self._model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                do_sample=True,
                pad_token_id=self._tokenizer.eos_token_id,
                eos_token_id=self._tokenizer.eos_token_id,
            )
            return self._tokenizer.decode(output_ids[0], skip_special_tokens=True)
        except Exception as e:
            return f"Error during text generation: {e}"

    # Expose tokenizer and model safely (if needed)
    # @property
    # def tokenizer(self):
    #     return self._tokenizer
    
    # @property
    # def model(self):
    #     return self._model
    
    # @property
    # def device(self):
    #     return self._device