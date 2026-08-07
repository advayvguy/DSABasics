from printing_tasks import Printer
from printing_tasks import Task
from queue import Queue
import random 
'''
    10 students - 20 tasks
    each task could have a random number of pages from 1 to 20 
    now there are 20 tasks in 1 hour or 3600 seconds or one task every 180 seconds
    well 20 tasks is the limit, but if we are lucky we might enncounter more than 20 tasks
    no checks in that regard 
'''

def new_task():
    num = random.randrange(1,181)
    return num == 180

def simulation(num_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    printing_queue = Queue()
    wait_times = []

    for current_second in range (num_seconds):
        
        if new_task():
            task = Task(current_second) #that task could have any number of pages 
            printing_queue.enqueue(task)

        if (not printer.busy()) and (not printing_queue.is_empty()):
            nexttask = printing_queue.dequeue()
            wait_times.append(nexttask.wait_time(current_second))
            printer.start_next(nexttask)

        printer.tick()

    avg_wait = sum(wait_times) / len(wait_times)
    print(f"Average Wait: {avg_wait:6.2f} seconds, tasks remaining: {printing_queue.size()}")

for i in range (20):
    simulation(3600, 5)
