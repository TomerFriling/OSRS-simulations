from data_tables import *
from single_rumour import *

total_catches = {
    "red_chinchompa": 0,
    "Herbiboar": 0,
    "tecu_salamander": 0,
    "dashing_kebbit": 0,
}

total_tasks = {
    "red_chinchompa": 0,
    "Herbiboar": 0,
    "tecu_salamander": 0,
    "dashing_kebbit": 0
}


def one_run(start_xp=13000000, end_xp=200000000):
    current_task = 'start'
    while start_xp < end_xp:
        current_task = generate_task(current_task)
        total_tasks[current_task] += 1
        counter = catch_counter(current_task)
        start_xp += xp_calculator(counter, current_task)
        total_catches[current_task] += counter

