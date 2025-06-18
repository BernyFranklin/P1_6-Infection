# GUI Tool Kit and Tool
import tkinter as tk
from tkinter import ttk

# Builds the control panel for a parent widget
def create_controls(parent):
    outer_frame = ttk.Frame(parent, padding = "10")     # Creates an outer frame, like a literal frame
    flex_frame = ttk.Frame(outer_frame)                 # Creates an inner frame, like the border on a nice frame that holds the art
    flex_frame.pack(anchor = "center")                  # Centers all the content and keeps it that way when window is resized

    # Dictionary that holds the parameter labels and dummy values
    params = {
        "Population Size": tk.IntVar(value = 100),
        "Initial Infected": tk.IntVar(value = 5),
        "Infection Rate": tk.DoubleVar(value = 25.0),
        "Recovery Time": tk.IntVar(value = 100),
        "Movement Speed": tk.DoubleVar(value = 2.0)
    }

    # Create the labels and text areas
    for label, var in params.items():
        group = ttk.Frame(flex_frame)                               # Assign content to a group
        group.pack(side = "left", padx = 5)                         # Content is left oriented
        ttk.Label(group, text = label).pack(anchor = "w")           # Create label, left oriented
        ttk.Entry(group, textvariable = var, width = 10).pack()     # Create text area
    
    # Dummy Buttons 
    button_group = ttk.Frame(flex_frame)                            # Buttons belong to the same frame
    button_group.pack(side = "left", padx = 20)                     # Left oriented with some space from the user input

    # Actual buttons that print their command when pressed, this will be modified later
    ttk.Button(button_group, text = "Start", command=lambda: print("Start")).pack(side = "left", padx = 2)
    ttk.Button(button_group, text = "Pause", command=lambda: print("Pause")).pack(side = "left", padx = 2)
    ttk.Button(button_group, text = "Reset", command=lambda: print("Reset")).pack(side = "left", padx = 2)

    # Return the control center
    return outer_frame, params