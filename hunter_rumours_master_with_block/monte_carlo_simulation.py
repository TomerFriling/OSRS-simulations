from single_rumour import *
from evaluation_matrices import *

total_catches = {
    "red_chinchompa": 0,
    "herbiboar": 0,
    "tecu_salamander": 0,
    "dashing_kebbit": 0,
}

total_tasks = {
    "red_chinchompa": 0,
    "herbiboar": 0,
    "tecu_salamander": 0,
    "dashing_kebbit": 0
}

current_prices = {
    "red_chinchompa": 1250,
    "herbiboar": 10000,
    "rumours": 24500
}


def one_run(start_xp=13000000, end_xp=200000000):
    current_task = 'start'
    while start_xp < end_xp:
        current_task = generate_task(current_task)
        total_tasks[current_task] += 1
        counter = catch_counter(current_task)
        start_xp += xp_calculator(counter, current_task)
        total_catches[current_task] += counter


number_of_simulations = 1000

for _ in range(number_of_simulations):
    one_run(start_xp=30000000)

total_catches = {k: v / number_of_simulations for k, v in total_catches.items()}
total_tasks = {k: v / number_of_simulations for k, v in total_tasks.items()}
gains = {key: current_prices[key] * total_catches[key] for key in current_prices.keys() if key != "rumours"}
gains["rumours"] = current_prices["rumours"] * sum(total_tasks.values())
gains = {k: v / 1e6 for k, v in gains.items()}

plot_task_counts_with_pie(total_catches, save_path="catches_count.png", title="Catches Counts and Probabilities",
                          show_total=False)
plot_task_counts_with_pie(total_tasks, save_path="task_count.png", title="Task Counts and Probabilities")
plot_task_counts_with_pie(gains, save_path="money_count.png", title="Money Counts and Probabilities [millions of GP]")