import tkinter as tk
from tkinter import ttk
from controls import create_controls
from simulation_canvas import SimulationCanvas
from graph import SIRGraph
from simulation_engine import SIRSimulation

def main():
    # Set up root
    root = tk.Tk()
    root.title("SIR Infection Simulation")
    root.resizable(True, True)                  # Needs to be True for use on laptop displays, otherwise its tiny
    root.grid_rowconfigure(1, weight = 1)
    root.grid_columnconfigure(0, weight = 1)

    # Controls on top
    controls_frame, params = create_controls(root)
    controls_frame.grid(row = 0, column = 0, sticky = "ew", padx = 10, pady = (10, 5))

    # Set up simulation and graph area
    sim_and_graph = ttk.Frame(root, padding = 10)
    sim_and_graph.grid(row = 1, column = 0)
    sim_and_graph.grid_columnconfigure(0, weight = 1)
    sim_and_graph.grid_columnconfigure(1, weight = 1)
    sim_and_graph.grid_rowconfigure(0, weight = 1)

    # Canvas on the left
    canvas = SimulationCanvas(sim_and_graph)
    canvas.grid(row = 0, column = 0, sticky = "nsew", padx = (10, 20))

    # Graph on the right
    graph = SIRGraph(sim_and_graph)
    graph.grid(row = 0, column = 1, sticky = "nsew", padx = 10)

    # Initialize simulation engine
    simulation = SIRSimulation(width = 400, height = 700)
    simulation.population_size = int(params["Population Size"].get())
    simulation.initial_infected = int(params["Initial Infected"].get())
    simulation.infection_rate = float(params["Infection Rate"].get())
    simulation.recovery_time = int(params["Recovery Time"].get())
    simulation.movement_speed = float(params["Movement Speed"].get())
    simulation.initialize_population()

    # Debug print to confirm values
    s, i, r = simulation.count_states()
    print(f"Initial counts - S: {s}, I: {i}, R: {r}")

    # Stats label or graph placeholder
    status_label = tk.Label(root, text = "Time: 0 | S: 0 | I: 0 | R: 0", padx = 5)
    status_label.grid(row = 2, column = 0, sticky = "w", padx = 10)

    root.mainloop()

if __name__ == "__main__":
    main()