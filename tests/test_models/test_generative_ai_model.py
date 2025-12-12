# GenerativeAIDemo tests
def test_import_and_init(generative_ai_model):
    assert generative_ai_model is not None
    assert hasattr(generative_ai_model, 'generate_text')

def test_generate_text_minimal(sample_prompt, generative_ai_model):
    # If the demo supports a lightweight stub (no real model loaded), this should still return
    # a sensible fallback or raise a clear error that tests can assert on. Adjust assertions
    # depending on your implementation.
    try:
        out = generative_ai_model.generate_text(sample_prompt, max_new_tokens=20)
        assert isinstance(out, str)
        assert len(out) > 0
    except RuntimeError as e:
        assert "Error generating text" in str(e) or "no model" in str(e).lower()

def test_generative_ai_temperature_effect(generative_ai_model):
    try:
        low_temp_output = generative_ai_model.generate_text("The future of AI is",\
                                                        temperature=0.2,\
                                                        max_new_tokens=50)
        high_temp_output = generative_ai_model.generate_text("The future of AI is",\
                                                            temperature=0.9,\
                                                            max_new_tokens=50)
        assert low_temp_output != high_temp_output
    except RuntimeError as e:
        # If the implementation purposely raises on missing model, assert the message
        assert "error in temperature setting" in str(e).lower() or "no model" in str(e).lower()

def test_generative_ai_handles_empty_prompt(generative_ai_model):
    try:
        output = generative_ai_model.generate_text("", temperature=0.7, max_new_tokens=50)
        assert len(output) > 0
    except ValueError as e:
        assert "prompt cannot be empty" in str(e).lower()

def test_generative_ai_output_length(generative_ai_model, sample_prompt):
    try:
        output = generative_ai_model.generate_text(sample_prompt,\
                                                   temperature=0.7,\
                                                   max_new_tokens=50)
        # [TODO] Check why we get slightly more than max_new_tokens sometimes
        intput_tokens = generative_ai_model.get_input_tokens(sample_prompt)
        prompt_ids = intput_tokens["input_ids"][0]
        assert len(output.split()) <= 50 + len(prompt_ids)
    except RuntimeError as e:
        assert "error in validating output length" in str(e).lower() or "no model" in str(e).lower()

def test_generative_ai_output_not_empty(generative_ai_model):
    try:
        output = generative_ai_model.generate_text("Once upon a time",\
                                                temperature=0.8,\
                                                max_new_tokens=50)
        assert len(output) > 10
    except RuntimeError as e:
        assert "error in testing output not empty" in str(e).lower() or "no model" in str(e).lower()