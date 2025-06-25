import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from sacred_mirror import (
    ArchitectAgent, MirrorAgent, GuideAgent,
    SacredRouter, MemoryEngine, mCP,
    ContextEnricher, OutputHarmonizer
)

# Load tokenizer and model (CPU-only)
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
print(">> Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print(">> Loading model to CPU...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map={"": "cpu"}  # Full CPU load — stable
)
print(">> Model loaded successfully.")

# LLM Query Function
def query_llm(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Set up Trivium Core
memory = MemoryEngine()
cp = mCP(memory)
architect = ArchitectAgent(mcp=cp)
mirror = MirrorAgent(mcp=cp)
guide = GuideAgent(mcp=cp)
router = SacredRouter(architect, mirror, guide)
enricher = ContextEnricher()
harmonizer = OutputHarmonizer()

# Unified chat pipeline
def trivium_chat(user_input):
    context = {
        "user_profile": {"tone": "strategic", "history": []},
        "ethics_profile": {"core_values": ["clarity", "respect", "truth"]},
    }
    reflected = router.process(user_input, context)
    enriched_prompt = enricher.enrich(user_input, reflected)
    raw_response = query_llm(enriched_prompt)
    return harmonizer.harmonize(raw_response, reflected)

# Gradio Interface
demo = gr.Interface(
    fn=trivium_chat,
    inputs=gr.Textbox(lines=5, placeholder="Ask or express anything..."),
    outputs="text",
    title="Trivium: The Agentic SDK Demo",
    description="This interface shows how Trivium interprets your input through structural, emotional, and ethical lenses before passing it to a language model."
)

# Run App
print(">> Launching Gradio server...")
demo.launch()
