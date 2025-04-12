import tkinter as tk
import random

# Constants for canvas size and cell grid
grid_size = 20
cell_size = 30
canvas_width = grid_size * cell_size
canvas_height = grid_size * cell_size

# List of colors to choose from
colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]

def erase(event):
    """Changes the color of cells under the eraser to white."""
    x, y = event.x, event.y
    
    # Get row and column index of the cell under eraser
    col = x // cell_size
    row = y // cell_size
    
    # Create a unique key for the rectangle in the canvas
    rect_id = (row, col)
    
    # If the cell is in the grid, erase it
    if rect_id in cells:
        canvas.itemconfig(cells[rect_id], fill="white")

def main():
    global canvas, cells
    
    root = tk.Tk()
    root.title("Eraser Canvas")
    
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    # Dictionary to store rectangles
    cells = {}
    
    # Draw the grid with random colors
    for row in range(grid_size):
        for col in range(grid_size):
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            color = random.choice(colors)  # Assign a random color to each cell
            rect = canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            cells[(row, col)] = rect
    
    # Bind mouse movement to erase function
    canvas.bind("<B1-Motion>", erase)
    
    root.mainloop()

if __name__ == "__main__":
    main()
