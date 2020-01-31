from injector import inject

from download_runner.download_runner import DownloadRunner
from input_manager.input_manager import InputManager
from request_scheduler import RequestScheduler


class DownloadManager:
    @inject
    def __init__(self, input_manager: InputManager, runner: DownloadRunner, request_scheduler: RequestScheduler):
        self.input_manager = input_manager
        self.runner = runner
        self.request_scheduler = request_scheduler

    def run(self):
        while True:
            if not self.request_scheduler.poll_stock():
                continue
            stock = self.input_manager.get_next()
            if stock is None:
                break
            # cont
            self.runner.run(stock)
