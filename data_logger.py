import csv
import os
from datetime import datetime

# Global variable to store timestep data
_log_data = []

def init_log():
    global _log_data
    _log_data = []

def log_step(timestep, susceptible, infected, recovered):
    global _log_data
    _log_data.append({
        'timestep': timestep,
        'susceptible': susceptible,
        'infected': infected,
        'recovered': recovered
    })

def save_log(scenario_label="RapidOutbreak", directory="data"):
    global _log_data

    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{scenario_label}_{timestamp}.csv"
    filepath = os.path.join(directory, filename)

    with open(filepath, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['timestep', 'susceptible', 'infected', 'recovered'])
        writer.writeheader()
        writer.writerows(_log_data)

    print(f"Run saved to {filepath}")
