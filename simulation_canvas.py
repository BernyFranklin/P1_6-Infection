import tkinter as tk
class SimulationCanvas(tk.Canvas):
    def __init__(self, parent, width = 600, height = 400):
        super().__init__(parent, width = width, height = height, bg = "white")
        self.create_text(width//2, height//2, text = "Simulation Area", font = ("Arial", 16))