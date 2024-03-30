# pip install transformers accelerate
import torch
from transformers import pipeline
pipe = pipeline("text-generation", model="anakin87/gemma-2b-orpo", torch_dtype=torch.bfloat16, device_map="auto")
messages = [{"role": "user", "content": "Write a rap song on Vim vs VSCode."}]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False)
outputs = pipe(prompt, max_new_tokens=500, do_sample=True, temperature=0.7,  top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
