# [TODO] Enable these fixtures after updating UI tests to match recent code
# changes

# def test_import_and_init(neural_network_demo):
#     assert neural_network_demo is not None

# def test_neural_network_demo(neural_network_demo):
#     # This test ensures that the run_demo method executes without errors
#     try:
#         result = neural_network_demo.train_nn()
#         assert isinstance(result, type(None))  # run_demo does not return anything
#     except Exception as e:
#         assert False, f"neural network training raised an exception: {e}"