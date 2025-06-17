import tkinter as tk
from tkinter import ttk

def create_controls(parent):
    frame = ttk.Frame(parent, padding = "10")

    # Dummy parameter dictionary
    params = {
        "Population Size": tk.IntVar(value = 100),
        "Initial Infected": tk.IntVar(value = 5),
        "Infection Rate": tk.DoubleVar(value = 25.0),
        "Recovery Time": tk.IntVar(value = 100),
        "Movement Speed": tk.DoubleVar(value = 2.0)
    }

    row = 0
    for label, var in params.items():
        ttk.Label(frame, text = label).grid(row = row, column = 0, sticky = "w")
        ttk.Entry(frame, textvariable = var, width = 10).grid(row = row, column = 1, padx = 5)
        row += 1
    
    # Dummy Buttons
    ttk.Button(frame, text = "Start", command=lambda: print("Start")).grid(row = 0, column = 2, padx = 10)
    ttk.Button(frame, text = "Pause", command=lambda: print("Pause")).grid(row = 1, column = 2, padx = 10)
    ttk.Button(frame, text = "Reset", command=lambda: print("Reset")).grid(row = 2, column = 2, padx = 10)

    return frame, params