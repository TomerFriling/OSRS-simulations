from data_tables import complete_probability, xp_table
import random


def catch_counter(task: str):
    counter = 0
    while True:
        counter += 1
        if random.randint(1, complete_probability[task]) == 1:
            return counter


def generate_task(previous_task: str, chin_is_blocked=False):
    next_task = ["herbiboar", "dashing_kebbit"]
    if not chin_is_blocked:
        next_task = ["herbiboar", "dashing_kebbit"] + ["red_chinchompa"]

    if previous_task == "tecu_salamander":
        return random.choice(next_task)
    return random.choice(next_task + ["tecu_salamander"])


def xp_calculator(catches: int, task: str):
    return catches * xp_table[task] + xp_table["master_rumour"]
