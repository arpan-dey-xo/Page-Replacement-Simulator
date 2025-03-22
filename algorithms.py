def simulate_fifo(pages, capacity):
    memory = []
    steps = []
    page_faults = 0
    for i, page in enumerate(pages, start=1):
        memory_before = memory.copy()
        fault = False
        removed = None
        if page not in memory:
            fault = True
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                removed = memory.pop(0)
                memory.append(page)
        memory_after = memory.copy()
        steps.append({
            'step': i,
            'page': page,
            'memory_before': memory_before,
            'fault': fault,
            'removed': removed,
            'memory_after': memory_after
        })
    return steps, page_faults

def simulate_lru(pages, capacity):
    memory = []
    steps = []
    page_faults = 0
    last_used = {}
    for i, page in enumerate(pages, start=1):
        memory_before = memory.copy()
        fault = False
        removed = None
        if page not in memory:
            fault = True
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: last_used.get(p, -1))
                removed = lru_page
                memory.remove(lru_page)
                memory.append(page)
        last_used[page] = i
        memory_after = memory.copy()
        steps.append({
            'step': i,
            'page': page,
            'memory_before': memory_before,
            'fault': fault,
            'removed': removed,
            'memory_after': memory_after
        })
    return steps, page_faults

def simulate_optimal(pages, capacity):
    memory = []
    steps = []
    page_faults = 0
    for i, page in enumerate(pages, start=1):
        memory_before = memory.copy()
        fault = False
        removed = None
        if page not in memory:
            fault = True
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                farthest = -1
                page_to_remove = None
                for mem_page in memory:
                    try:
                        next_use = pages[i:].index(mem_page)
                    except ValueError:
                        page_to_remove = mem_page
                        break
                    if next_use > farthest:
                        farthest = next_use
                        page_to_remove = mem_page
                removed = page_to_remove
                memory.remove(page_to_remove)
                memory.append(page)
        memory_after = memory.copy()
        steps.append({
            'step': i,
            'page': page,
            'memory_before': memory_before,
            'fault': fault,
            'removed': removed,
            'memory_after': memory_after
        })
    return steps, page_faults

def fifo(pages, capacity):
    steps, faults = simulate_fifo(pages, capacity)
    return faults

def lru(pages, capacity):
    steps, faults = simulate_lru(pages, capacity)
    return faults

def optimal(pages, capacity):
    steps, faults = simulate_optimal(pages, capacity)
    return faults