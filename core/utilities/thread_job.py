import threading
from typing import Any


class ThreadJob(threading.Thread):
    def __init__(self, callback, event: Any, interval: int):
        """runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: number in day after which are required to fire the callback
        :type callback: function
        :type interval: int
        """

        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob,self).__init__()

    def run(self):
        day_interval = self.interval * 60 * 60 * 24
        while not self.event.wait(self.interval):
            self.callback()
