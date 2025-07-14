# GUI Tool Kit
import tkinter as tk

# Define custom class that inherits tk.canvas
class SimulationCanvas(tk.Canvas):
    # Intitializes a blank white 400x700 canvas
    def __init__(self, parent, width = 400, height = 700):
        super().__init__(parent, width = width, height = height, bg = "white")
        # Placeholder that shows content inside the canvas
        self.create_text(width//2, height//2, font = ("Arial", 16), fill = "black")