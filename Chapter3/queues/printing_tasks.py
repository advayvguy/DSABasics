from queue import Queue
import random 

class Printer:
    def __init__(self,ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_left = 0

    def tick(self):
        if self.current_task is not None:
            self.time_left = self.time_left - 1
            if self.time_left <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_left = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


