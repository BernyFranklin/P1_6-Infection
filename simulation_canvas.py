import tkinter as tk
class SimulationCanvas(tk.Canvas):
    def __init__(self, parent, width = 400, height = 700):
        super().__init__(parent, width = width, height = height, bg = "white")
        self.create_text(width//2, height//2, text = "Simulation Area", font = ("Arial", 16))
        self.pack_propagate(False)
        self.canvas = tk.Canvas(self, bg = "white")
        self.canvas.pack(fill = tk.BOTH, expand = True)