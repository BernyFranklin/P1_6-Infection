import tkinter as tk
from tkinter import ttk

def create_controls(parent):
    outer_frame = ttk.Frame(parent, padding = "10")
    flex_frame = ttk.Frame(outer_frame)
    flex_frame.pack(anchor = "center", pady = 5)

    # Dummy parameter dictionary
    params = {
        "Population Size": tk.IntVar(value = 100),
        "Initial Infected": tk.IntVar(value = 5),
        "Infection Rate": tk.DoubleVar(value = 25.0),
        "Recovery Time": tk.IntVar(value = 100),
        "Movement Speed": tk.DoubleVar(value = 2.0)
    }

    # User Input Section
    for label, var in params.items():
        group = ttk.Frame(flex_frame)
        group.pack(side = "left", padx = 5)
        ttk.Label(group, text = label).pack(anchor = "w")
        ttk.Entry(group, textvariable = var, width = 10).pack()
    
    # Dummy Buttons 
    button_group = ttk.Frame(flex_frame)
    button_group.pack(side = "left", padx = 20)

    ttk.Button(button_group, text = "Start", command=lambda: print("Start")).pack(side = "left", padx = 2)
    ttk.Button(button_group, text = "Pause", command=lambda: print("Pause")).pack(side = "left", padx = 2)
    ttk.Button(button_group, text = "Reset", command=lambda: print("Reset")).pack(side = "left", padx = 2)

    return outer_frame, params