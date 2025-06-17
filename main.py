import tkinter as tk
from controls import create_controls
from simulation_canvas import SimulationCanvas

def main():
    root = tk.Tk()
    root.title("SIR Infection Simulation")

    # Controls on top
    controls_frame, params = create_controls(root)
    controls_frame.pack(side=tk.TOP, fill=tk.X)

    # Canvas
    sim_canvas = SimulationCanvas(root, width = 600, height = 400)
    sim_canvas.pack(pady = 10)

    # Stats label or graph placeholder
    stats_label = tk.Label(root, text = "S: 0 | I: 0 | R:0")
    stats_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()