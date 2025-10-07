import matplotlib.pyplot as plt
import os


def money(current_prices: dict, all_catches: dict):
    total_money = {
        "red_chinchompa": 0,
        "herbiboar": 0,
        "rumours": 0
    }
    total = 0
    for key in current_prices:
        total_money[key] = current_prices[key] * all_catches[key]
        total += total_money[key]
    return total_money, total


def plot_task_counts_with_pie(to_plot, save_path="task_counts.png",
                              title="Task Counts and Probabilities",
                              show_total=True):
    task_names = list(to_plot.keys())
    counts = list(to_plot.values())

    total = sum(counts)
    probs = [c / total for c in counts] if total > 0 else [0 for _ in counts]

    # Create side-by-side plots: bar (left) and pie (right)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # === Bar chart ===
    bars = axes[0].bar(task_names, counts, color="skyblue", edgecolor="black")
    for bar, prob in zip(bars, probs):
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{prob * 100:.1f}%",
            ha='center', va='bottom', fontsize=10, color="darkblue"
        )
    axes[0].set_ylabel("Count")
    axes[0].set_title(title)
    axes[0].set_xticks(range(len(task_names)))
    axes[0].set_xticklabels([name.replace("_", " ") for name in task_names], rotation=20)

    # === Pie chart ===
    wedges, texts, autotexts = axes[1].pie(
        counts,
        labels=[name.replace("_", " ") for name in task_names],
        autopct=lambda p: f"{int(round(p * total / 100))}",  # absolute counts
        colors=plt.cm.Set3.colors,
        startangle=90
    )
    axes[1].set_title("Distribution (counts)")

    # === Add total count if requested ===
    if show_total:
        fig.suptitle(f"{title} — Total = {int(total)}", fontsize=12, y=1.02)

    plt.tight_layout()

    os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"💾 Saved combined bar+pie plot to: {save_path}")


