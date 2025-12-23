# Abstract base class thread
from PySide6.QtCore import QThread, Signal
from utils.threads.thread_sync_primitives import PauseResume, StopSignal

class ThreadBaseWorker(QThread):
    finished = Signal()
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.pause_resume = PauseResume()
        self.stop_signal = StopSignal()

    def pause(self):
        self.pause_resume.pause()

    def resume(self):
        self.pause_resume.resume()

    def stop(self):
        if not self.stop_signal.is_stopped():
            self.stop_signal.stop()

    # Thread execution starts with this function
    def run(self):
        try:
            self.execute()
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()

    def execute(self):
        """
        Override this method in child classes
        """
        raise NotImplementedError