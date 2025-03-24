import matplotlib.pyplot as plt
from algorithms import simulate_fifo, simulate_lru, simulate_optimal

def run_simulation_detailed(pages_str, capacity, algorithm):
    """
    Returns a tuple: (simulation steps list, total page fault count)
    """
    try:
        pages = [int(x.strip()) for x in pages_str.split(",") if x.strip() != ""]
    except Exception as e:
        return f"Error parsing pages: {e}", None

    algorithm = algorithm.upper()
    if algorithm == "FIFO":
        steps, faults = simulate_fifo(pages, capacity)
    elif algorithm == "LRU":
        steps, faults = simulate_lru(pages, capacity)
    elif algorithm == "OPTIMAL":
        steps, faults = simulate_optimal(pages, capacity)
    else:
        return "Unknown algorithm. Please select FIFO, LRU, or Optimal.", None
    return steps, faults

def plot_graph(results):
    algorithms = list(results.keys())
    page_faults = list(results.values())

    plt.bar(algorithms, page_faults, color=["skyblue", "lightgreen", "salmon"])
    plt.xlabel("Page Replacement Algorithms")
    plt.ylabel("Number of Page Faults")
    plt.title("Comparison of Page Faults")
    plt.tight_layout()
    plt.show()

def run_simulation(pages_str, capacity, algorithm):
    try:
        pages = [int(x.strip()) for x in pages_str.split(",") if x.strip() != ""]
    except Exception as e:
        return f"Error parsing pages: {e}"

    results = {}
    steps_fifo, faults_fifo = simulate_fifo(pages, capacity)
    results['FIFO'] = faults_fifo

    steps_lru, faults_lru = simulate_lru(pages, capacity)
    results['LRU'] = faults_lru

    steps_opt, faults_opt = simulate_optimal(pages, capacity)
    results['Optimal'] = faults_opt

    plot_graph(results)

    return results[algorithm.upper()]
