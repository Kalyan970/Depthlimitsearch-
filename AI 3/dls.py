import tkinter as tk
from tkinter import messagebox
import time

def depth_limited_search(graph, start, goal, depth_limit):
    visited = set()
    path = []
    draw_graph(graph, path)  # Initial draw
    found = dls_recursive(graph, start, goal, depth_limit, visited, path)
    return found, path

def dls_recursive(graph, node, goal, depth_limit, visited, path, depth=0):
    path.append(node)
    draw_graph(graph, path, node, highlight="yellow")
    root.update()
    time.sleep(1)

    if node == goal:
        return True
    if depth >= depth_limit:
        path.pop()
        draw_graph(graph, path, node, highlight="red")
        root.update()
        time.sleep(1)
        return False
    if node in visited:
        path.pop()
        draw_graph(graph, path, node, highlight="red")
        root.update()
        time.sleep(1)
        return False

    visited.add(node)
    for neighbor in graph[node]:
        if dls_recursive(graph, neighbor, goal, depth_limit, visited, path, depth + 1):
            return True

    path.pop()
    draw_graph(graph, path, node, highlight="red")
    root.update()
    time.sleep(1)
    return False

def run_dls():
    graph = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['D', 'I'],
        'C': ['E', 'F'],
        'D': ['G'],
        'I': ['H', 'J'],
        'E': [], 'F': [], 'G': [], 'H': [], 'J': []
    }

    start_node = start_entry.get()
    goal_node = goal_entry.get()
    depth_limit = int(depth_entry.get())

    found, path = depth_limited_search(graph, start_node, goal_node, depth_limit)
    if found:
        messagebox.showinfo("Result", f"Goal found within depth limit. Path taken: {' -> '.join(path)}")
    else:
        messagebox.showinfo("Result", f"Goal not found within depth limit. Path taken: {' -> '.join(path)}")

    draw_graph(graph, path)

def draw_graph(graph, path, current_node=None, highlight=None):
    canvas.delete("all")  # Clear the canvas

    # Define positions for each node
    positions = {
        'S': (200, 50),
        'A': (100, 150),
        'B': (300, 150),
        'C': (50, 250),
        'D': (150, 250),
        'E': (20, 350),
        'F': (80, 350),
        'G': (150, 350),
        'H': (300, 350),
        'I': (350, 250),
        'J': (400, 350)
    }

    # Draw edges
    for node in graph:
        for neighbor in graph[node]:
            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]
            canvas.create_line(x1, y1, x2, y2)

    # Draw nodes
    for node, (x, y) in positions.items():
        color = "white"
        if node in path:
            color = "yellow"
        if node == current_node and highlight:
            color = highlight
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)
        canvas.create_text(x, y, text=node)

    # Highlight path
    for i in range(len(path) - 1):
        x1, y1 = positions[path[i]]
        x2, y2 = positions[path[i + 1]]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

# Create main window
root = tk.Tk()
root.title("Depth-Limited Search")

# Create input fields and labels
start_label = tk.Label(root, text="Start Node:")
start_label.grid(row=0, column=0)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1)

goal_label = tk.Label(root, text="Goal Node:")
goal_label.grid(row=1, column=0)
goal_entry = tk.Entry(root)
goal_entry.grid(row=1, column=1)

depth_label = tk.Label(root, text="Depth Limit:")
depth_label.grid(row=2, column=0)
depth_entry = tk.Entry(root)
depth_entry.grid(row=2, column=1)

# Create button to run search
search_button = tk.Button(root, text="Run DLS", command=run_dls)
search_button.grid(row=3, columnspan=2)

# Create canvas to draw graph
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.grid(row=4, columnspan=2)

# Start the GUI event loop
root.mainloop()
