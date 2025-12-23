# A dedicated class for thread sync primitives
import threading

class PauseResume:
    def __init__(self):
        """A class to pause and resume events"""
        self._pause_event = threading.Event()
        self._pause_event.set()

    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()

    def wait(self):
        self._pause_event.wait()

class StopSignal:
    def __init__(self):
        """A class to manage stop events"""
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def is_stopped(self):
        return self._stop_event.is_set()