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

    # User Input Section (Rows 0 and 1)
    col = 0
    for label, var in params.items():
        ttk.Label(frame, text = label).grid(row = 0, column = col, sticky = "w", padx = 5)
        ttk.Entry(frame, textvariable = var, width = 10).grid(row = 1, column = col, padx = 5)
        col += 1
    
    # Spacer Row (Row 2)
    ttk.Label(frame, text = "").grid(row = 2, column = 0, pady = 10)

    # Dummy Buttons (Row 3)
    ttk.Button(frame, text = "Start", command=lambda: print("Start")).grid(row = 3, column = 1, padx = 5)
    ttk.Button(frame, text = "Pause", command=lambda: print("Pause")).grid(row = 3, column = 2, padx = 5)
    ttk.Button(frame, text = "Reset", command=lambda: print("Reset")).grid(row = 3, column = 3, padx = 5)

    return frame, params