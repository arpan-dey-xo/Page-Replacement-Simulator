# Page-Replacement-Simulator
### 📌 Project Overview
This project is a Page Replacement Simulator designed to help understand how different page replacement strategies work in an Operating System's virtual memory management.
### 🧸 Simple Explanation
Imagine you have a small bag (memory) that can only hold a limited number of books (pages). But you have a huge bookshelf (hard drive) full of books. If you need a book that isn’t in your bag, you must remove an old book to make space for the new one. The question is: which book should you remove?

Different strategies (algorithms) answer this question in different ways, like:
- FIFO (First In, First Out) – Remove the oldest book first.
- LRU (Least Recently Used) – Remove the book you haven’t read for the longest time.
- Optimal (OPT) – Remove the book that you won’t need for the longest time in the future (perfect but unrealistic).
This simulator will allow you to test these strategies with sample data and see how efficient they are.
### 🖥️ Technical Explanation
This project simulates page replacement algorithms used in demand paging in virtual memory systems. It tracks page faults, where a page needed by a process is not in the main memory and must be loaded from secondary storage.
### ✨ Features
- Simulates FIFO, LRU, Optimal (OPT) page replacement algorithms.
- Takes input as page reference sequences and frame size.
- Displays step-by-step execution of the algorithms.
- Shows page fault count and efficiency comparison.
- Provides a Graphical User Interface (GUI) for easy interaction.
### ⚙️ Tech Stack
- Programming Language: Python
- Libraries:
  - tkinter (for GUI)
- Execution Mode: Graphical User Interface (GUI)
### 🏗️ Project Structure
This project is divided into three main modules:
1. GUI Module (gui.py)
- Uses Tkinter to create a user-friendly interface.
- Allows users to input page reference sequences and choose an algorithm.
- Displays step-by-step execution and a visual representation of memory frames.
2. Page Replacement Logic (algorithms.py)
- Implements FIFO, LRU, and Optimal algorithms.
- Returns page fault counts and memory state at each step.
- Acts as the backend for the GUI.
3. Simulation Controller (controller.py)
- Acts as the bridge between GUI and Algorithms.
- Calls the appropriate page replacement function.
- Formats and sends the results to the GUI for display.
4. Entry Point (main.py)
- Serves as the entry point that launches the GUI.
### 🚀 How It Works Internally
- User inputs a sequence of page requests and memory frame size via the GUI.
- The controller module processes the input and calls the appropriate algorithm.
- The algorithm module executes the logic and calculates page faults.
- The GUI displays step-by-step memory updates and final results.
### 📌 Future Enhancements
- Visualizations using matplotlib.
- Support for additional algorithms (LFU, CLOCK etc.)
- More interactive GUI with animations
### 📜 License
MIT License
### 🤓 Contributors
- Arpan Dey - [Connect](https://github.com/arpan-dey-xo)
- Podugu Nishanth - [Connect](https://github.com/nishanth-podugu)
