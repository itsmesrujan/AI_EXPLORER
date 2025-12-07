# [TODO] Enable these fixtures after updating UI tests to match recent code
# changes

# def test_import_and_init(kmeans_demo):
#     assert kmeans_demo is not None

# def test_kmeans_run_demo(kmeans_demo):
#     # This test ensures that the run_demo method executes without errors
#     try:
#         result = kmeans_demo.run_demo()
#         assert isinstance(result, type(None))  # run_demo does not return anything
#     except Exception as e:
#         assert False, f"kmeans run_demo raised an exception: {e}"