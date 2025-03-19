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

def run_simulation(pages_str, capacity, algorithm):
    steps, faults = run_simulation_detailed(pages_str, capacity, algorithm)
    return faults