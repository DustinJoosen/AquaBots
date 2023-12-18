import threading
import time


class SetInterval:
    def __init__(self, action, interval, **kwargs):
        self.action = action
        self.interval = interval
        self.kwargs = kwargs
        self.stopEvent = threading.Event()

        thread = threading.Thread(target=self._set_interval)
        thread.start()

    def _set_interval(self):
        next_time = time.time() + self.interval
        while not self.stopEvent.wait(next_time - time.time()):
            next_time += self.interval
            self.action(**self.kwargs)

    def cancel(self):
        self.stopEvent.set()

