import tkinter as tk
from tkinter import ttk, messagebox
from controller import run_simulation_detailed, run_simulation

def run_sim():
    pages_str = pages_entry.get()
    capacity_str = capacity_entry.get()
    algorithm = algo_var.get()
    if not pages_str or not capacity_str:
        messagebox.showerror("Input Error", "Please enter both page sequence and capacity.")
        return
    try:
        capacity = int(capacity_str)
    except ValueError:
        messagebox.showerror("Input Error", "Capacity must be an integer.")
        return

    for row in table.get_children():
        table.delete(row)

    result = run_simulation_detailed(pages_str, capacity, algorithm)
    if isinstance(result[0], str):
        messagebox.showerror("Error", result[0])
        return
    steps, faults = result
    output_var.set(f"{algorithm} Page Faults: {faults}")
    
    for step in steps:
        table.insert("", "end", values=(
            step['step'],
            step['page'],
            ", ".join(map(str, step['memory_before'])),
            "Yes" if step['fault'] else "No",
            step['removed'] if step['removed'] is not None else "",
            ", ".join(map(str, step['memory_after']))
        ))

    run_simulation(pages_str, capacity, algorithm)

app = tk.Tk()
app.title("Page Replacement Simulator")

tk.Label(app, text="Page Sequence (comma separated):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
pages_entry = tk.Entry(app, width=50)
pages_entry.grid(row=0, column=1, padx=5, pady=5)
pages_entry.insert(0, "7,0,1,2,0,3,4,2,3,0,3,2,1,2")

tk.Label(app, text="Memory Capacity:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
capacity_entry = tk.Entry(app, width=10)
capacity_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
capacity_entry.insert(0, "3")

tk.Label(app, text="Algorithm:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
algo_var = tk.StringVar(value="FIFO")
algo_options = ttk.Combobox(app, textvariable=algo_var, values=["FIFO", "LRU", "Optimal"], state="readonly")
algo_options.grid(row=2, column=1, sticky="w", padx=5, pady=5)

run_button = tk.Button(app, text="Run Simulation", command=run_sim)
run_button.grid(row=3, column=0, columnspan=2, pady=10)

output_var = tk.StringVar(value="Output will appear here")
output_label = tk.Label(app, textvariable=output_var, font=("Arial", 14))
output_label.grid(row=4, column=0, columnspan=2, pady=10)

table_frame = tk.Frame(app)
table_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

columns = ("Step", "Page", "Memory Before", "Fault", "Removed", "Memory After")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor="center")
table.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

app.mainloop()
