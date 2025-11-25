import pytest
from modules.generative_ai.generative_ai_page import GenerativeAIPage

def test_generative_ai_page_initialization():
    page = GenerativeAIPage()
    assert page.prompt_input is not None
    assert page.generate_btn is not None
    assert page.output_area is not None

# def test_generative_ai_page_ui_elements():
#     page = GenerativeAIPage()
#     assert page.layout().count() >= 5  # At least labels, input, button, output
#     assert isinstance(page.temp_box, QSpinBox)
#     assert page.temp_box.minimum() == 1
#     assert page.temp_box.maximum() == 10
#     assert page.temp_box.value() == 7

def test_generative_ai_page_run_generation_method_exists():
    page = GenerativeAIPage()
    assert hasattr(page, 'run_generation')
    assert callable(getattr(page, 'run_generation'))

def test_generative_ai_page_run_generation_updates_output_area(monkeypatch):
    page = GenerativeAIPage()
    def mock_generate_text(prompt, temperature=0.7, max_tokens=200):
        return "Generated text based on prompt."    
    monkeypatch.setattr(page.demo, 'generate_text', mock_generate_text)
    page.prompt_input.setText("Test prompt")
    page.temp_box.setValue(5)  # Set temperature to 0.5
    page.run_generation()
    assert page.output_area.toPlainText() == "Generated text based on prompt."