import pytest

@pytest.fixture(scope="module", autouse=True)
def setup_environment():
    # Setup code before any tests run
    print("\nSetting up test environment...")
    yield
    # Teardown code after all tests run
    print("\nTearing down test environment...")

@pytest.fixture
def sample_prompt():
    return "It's a bright sunny day in the city!"

@pytest.fixture
def generative_ai_model():
    from models.generative_ai import GenerativeAI
    return GenerativeAI()