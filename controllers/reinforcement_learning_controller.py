from models.reinforcement_learning import ReinforcementLearning

class ReinforcementLearningController():
    def __init__(self):
        'Controller class for Reinforcement Learning'
        self._reinforcementLearning_instance = ReinforcementLearning()
        self._grid, self._cmap, self._norm = None, None, None
        self._error_occurred, self._error_message = False, ''

    def _handle_error(self, error_msg):
        print(f"Thread error: {error_msg}")
        self._error_occurred = True
        self._error_message = error_msg

    def _get_learning_data(self):
        from controllers.controller_threads.thread_reinforcement_worker import ThreadReinforcementWorker
        self._worker_thread_instance = ThreadReinforcementWorker(self._reinforcementLearning_instance)
        self._worker_thread_instance.error.connect(self._handle_error)
        self._worker_thread_instance.start()
        # wait until thread finishes
        self._worker_thread_instance.wait()
        if self._worker_thread_instance is None:
            raise RuntimeError("Thread completed but no result was produced")
        return self._worker_thread_instance.result