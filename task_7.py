import random


def simulate_dice_rolls(n):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        dice_sum = roll_d6() + roll_d6()
        results[dice_sum] += 1

    return results, n


def roll_d6():
    return random.randint(1, 6)


def show_result_table(results, n):
    print("Monte-Carlo probabilities:")
    for key in sorted(results):
        total = results[key]
        print(f"{key}: {total / n * 100:.2f}% ({total}/{n})")


def get_analytic_probabilities():
    ways = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
        8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    return {s: ways[s] / 36 for s in range(2, 13)}


def show_comparison_table(results, n, analytic_probs):
    print(f"\nComparison: Monte-Carlo(n={n}) vs Analytic")
    print("{:<5} {:>9} {:>12} {:>12} {:>12}".format("Sum", "Count", "MC %", "Analytic %", "|Diff| %"))
    print("-" * 56)
    total_count = 0
    total_mc = 0
    total_an = 0
    total_diff = 0

    for s in range(2, 13):
        count = results[s]
        mc = (count / n) * 100
        an = analytic_probs[s] * 100
        diff = abs(mc - an)

        total_count += count
        total_mc += mc
        total_an += an
        total_diff += diff
        print("{:<5} {:>9} {:>11.2f}% {:>11.2f}% {:>11.2f}%".format(s, count, mc, an, diff))
    
    print("-" * 56)
    print("{:<5} {:>9} {:>11.2f}% {:>11.2f}% {:>11.2f}%".format("Total", total_count, total_mc, total_an, total_diff / 11))


def experiment(ns):
    analytic_probs = get_analytic_probabilities()
    for n in ns:
        results, n = simulate_dice_rolls(n)
        show_comparison_table(results, n, analytic_probs)



experiment([36, 1_000, 10_000, 100_000])
