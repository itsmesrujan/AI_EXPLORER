import pytest
from modules.generative_ai.generative_ai_demo import GenerativeAIDemo

def test_generative_ai_output_not_empty():
    demo = GenerativeAIDemo()
    output = demo.generate_text("Once upon a time", temperature=0.8, max_tokens=50)
    assert len(output) > 10

def test_generative_ai_temperature_effect():
    demo = GenerativeAIDemo()
    low_temp_output = demo.generate_text("The future of AI is", temperature=0.2, max_tokens=50)
    high_temp_output = demo.generate_text("The future of AI is", temperature=0.9, max_tokens=50)
    assert low_temp_output != high_temp_output

def test_generative_ai_handles_empty_prompt():
    demo = GenerativeAIDemo()
    output = demo.generate_text("", temperature=0.7, max_tokens=50)
    assert len(output) > 0