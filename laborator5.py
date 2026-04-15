import random
import time
import csv


# =========================================================
# CLASA PENTRU STATISTICI
# =========================================================
class Stats:
    def __init__(self):
        self.comparisons = 0
        self.moves = 0
        self.recursive_calls = 0


# =========================================================
# BUBBLE SORT
# =========================================================
def bubble_sort(arr, stats):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            stats.comparisons += 1

            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                stats.moves += 1
                swapped = True

        if not swapped:
            break

    return arr


# =========================================================
# QUICK SORT
# =========================================================
def quick_sort(arr, stats):
    stats.recursive_calls += 1

    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        stats.comparisons += 1
        if x < pivot:
            left.append(x)
            stats.moves += 1
        elif x == pivot:
            middle.append(x)
            stats.moves += 1
        else:
            right.append(x)
            stats.moves += 1

    return quick_sort(left, stats) + middle + quick_sort(right, stats)


# =========================================================
# MERGE SORT
# =========================================================
def merge_sort(arr, stats):
    stats.recursive_calls += 1

    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], stats)
    right = merge_sort(arr[mid:], stats)

    return merge(left, right, stats)


def merge(left, right, stats):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        stats.comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            stats.moves += 1
            i += 1
        else:
            result.append(right[j])
            stats.moves += 1
            j += 1

    while i < len(left):
        result.append(left[i])
        stats.moves += 1
        i += 1

    while j < len(right):
        result.append(right[j])
        stats.moves += 1
        j += 1

    return result


# =========================================================
# FUNCȚII UTILE
# =========================================================
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def same_elements(a, b):
    if len(a) != len(b):
        return False

    count_a = {}
    count_b = {}

    for x in a:
        count_a[x] = count_a.get(x, 0) + 1

    for x in b:
        count_b[x] = count_b.get(x, 0) + 1

    return count_a == count_b


# =========================================================
# GENERAREA DATELOR
# =========================================================
def generate_random_list(n):
    return [random.randint(0, 100000) for _ in range(n)]


def generate_sorted_list(n):
    return list(range(n))


def generate_reverse_sorted_list(n):
    return list(range(n, 0, -1))


def generate_duplicates_list(n):
    return [random.randint(0, 10) for _ in range(n)]


def generate_almost_sorted_list(n):
    arr = list(range(n))
    number_of_swaps = max(1, n // 20)  # aproximativ 5% dereglări

    for _ in range(number_of_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_test_data(n, data_type):
    if data_type == "aleator":
        return generate_random_list(n)
    elif data_type == "sortat crescator":
        return generate_sorted_list(n)
    elif data_type == "sortat descrescator":
        return generate_reverse_sorted_list(n)
    elif data_type == "duplicate":
        return generate_duplicates_list(n)
    elif data_type == "aproape sortat":
        return generate_almost_sorted_list(n)
    else:
        raise ValueError("Tip de intrare necunoscut.")


# =========================================================
# AFIȘAREA REZULTATELOR
# =========================================================
def print_results_table(results):
    header = (
        f"{'Algoritm':<12} {'Dimensiune':<10} {'Intrare':<20} "
        f"{'Timp mediu(s)':<15} {'Comparatii':<15} {'Mutari':<12} {'Apeluri rec.':<12}"
    )
    print(header)
    print("-" * len(header))

    for row in results:
        print(
            f"{row['algorithm']:<12} "
            f"{row['size']:<10} "
            f"{row['input_type']:<20} "
            f"{row['avg_time']:<15.6f} "
            f"{row['avg_comparisons']:<15.2f} "
            f"{row['avg_moves']:<12.2f} "
            f"{row['avg_recursive_calls']:<12.2f}"
        )


def save_results_to_csv(results, filename="rezultate_sortari.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Algoritm",
            "Dimensiune",
            "Tip intrare",
            "Timp mediu (s)",
            "Comparatii",
            "Mutari",
            "Apeluri recursive"
        ])

        for row in results:
            writer.writerow([
                row["algorithm"],
                row["size"],
                row["input_type"],
                row["avg_time"],
                row["avg_comparisons"],
                row["avg_moves"],
                row["avg_recursive_calls"]
            ])


# =========================================================
# TESTAREA UNUI ALGORITM
# =========================================================
def run_single_test(algorithm_name, algorithm_function, original_data):
    stats = Stats()
    data_copy = original_data.copy()

    start = time.perf_counter()
    result = algorithm_function(data_copy, stats)
    end = time.perf_counter()

    execution_time = end - start

    return result, execution_time, stats


# =========================================================
# PROGRAM PRINCIPAL
# =========================================================
def run_benchmark():
    random.seed(42)

    sizes = [100, 500, 1000, 2000, 3000]
    input_types = [
        "aleator",
        "sortat crescator",
        "sortat descrescator",
        "duplicate",
        "aproape sortat"
    ]

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort)
    ]

    runs_per_test = 3
    results = []

    for size in sizes:
        for input_type in input_types:
            original_data = generate_test_data(size, input_type)

            for algorithm_name, algorithm_function in algorithms:
                total_time = 0
                total_comparisons = 0
                total_moves = 0
                total_recursive_calls = 0

                for _ in range(runs_per_test):
                    sorted_result, execution_time, stats = run_single_test(
                        algorithm_name,
                        algorithm_function,
                        original_data
                    )

                    # verificare corectitudine
                    if not is_sorted(sorted_result):
                        print("Eroare: lista nu este sortată corect.")
                        print("Algoritm:", algorithm_name)
                        print("Dimensiune:", size)
                        print("Intrare:", input_type)
                        return

                    if not same_elements(sorted_result, original_data):
                        print("Eroare: elementele finale nu coincid cu cele inițiale.")
                        print("Algoritm:", algorithm_name)
                        print("Dimensiune:", size)
                        print("Intrare:", input_type)
                        return

                    total_time += execution_time
                    total_comparisons += stats.comparisons
                    total_moves += stats.moves
                    total_recursive_calls += stats.recursive_calls

                results.append({
                    "algorithm": algorithm_name,
                    "size": size,
                    "input_type": input_type,
                    "avg_time": total_time / runs_per_test,
                    "avg_comparisons": total_comparisons / runs_per_test,
                    "avg_moves": total_moves / runs_per_test,
                    "avg_recursive_calls": total_recursive_calls / runs_per_test
                })

    print_results_table(results)
    save_results_to_csv(results)

    print("\nRezultatele au fost salvate și în fișierul rezultate_sortari.csv")


if __name__ == "__main__":
    run_benchmark()