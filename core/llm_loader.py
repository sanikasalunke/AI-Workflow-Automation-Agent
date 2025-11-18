"""
Minimal LLM loader. Adjust model_path to your GGUF model location.
This example uses llama-cpp-python. If you use Ollama or other runtime,
replace the interface (method `generate_text(prompt)` must return string).
"""
from typing import Any, Dict
try:
    from llama_cpp import Llama
except Exception:
    Llama = None

class LLMWrapper:
    def __init__(self, model_path="models/phi3-mini.gguf", n_ctx=2048, n_threads=4):
        self.model_path = model_path
        self.n_ctx = n_ctx
        self.n_threads = n_threads
        self.model = None
        self._load()

    def _load(self):
        if Llama is None:
            raise RuntimeError("llama_cpp is not installed. Install llama-cpp-python or adapt loader.")
        self.model = Llama(model_path=self.model_path, n_ctx=self.n_ctx, n_threads=self.n_threads)

    def generate_text(self, prompt: str, max_tokens: int = 512, stop=None) -> str:
        resp = self.model.create(prompt=prompt, max_tokens=max_tokens, stop=stop)
        # llama-cpp-python returns dict with 'choices'
        return resp['choices'][0]['text']

def load_llm():
    """Call this to get an LLM wrapper instance."""
    return LLMWrapper()
