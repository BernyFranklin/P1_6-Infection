import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# matplotlib.use("Agg")

class SIRGraph(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a figure and axis
        self.fig, self.ax = plt.subplots(figsize = (5, 3.5), dpi = 100)
        self.fig.tight_layout()
        self.ax.set_title("SIR Model Over Time", fontsize = 10)
        self.ax.set_xlabel("Time Steps", fontsize = 9)
        self.ax.set_ylabel("Population", fontsize = 9)
        self.ax.tick_params(labelsize = 8)
        self.ax.grid(True)

        # Dummy time axis and initial lines
        self.x_data = list(range(100))
        self.s_data = [np.sin(x / 10) * 50 + 150 for x in self.x_data]
        self.i_data = [np.cos(x / 10) * 40 + 100 for x in self.x_data]
        self.r_data = [200 - s - i for s, i in zip(self.s_data, self.i_data)]

        self.s_line = self.ax.plot(self.x_data, self.s_data, label = "Susceptible", color = "blue")
        self.i_line = self.ax.plot(self.x_data, self.i_data, label = "Infected",    color = "red")
        self.r_line = self.ax.plot(self.x_data, self.r_data, label = "Recovered",   color = "green")

        self.ax.legend()

        # Embed in tkinter frame
        self.canvas = FigureCanvasTkAgg(self.fig, master = self)
        self.canvas.get_tk_widget().pack(fill = tk.BOTH, expand = True)
        self.canvas.draw()

    def update_graph(self, new_s, new_i, new_r):
        """Call this with new y-data lists to update graph"""
        if len(new_s) != len(self.x_data):
            print("[SIRGraph] Warning: Data length mismatch")
            return
        
        self.s_line.set_ydata(new_s)
        self.i_line.set_ydata(new_i)
        self.r_line.set_ydata(new_r)
        self.canvas.draw()