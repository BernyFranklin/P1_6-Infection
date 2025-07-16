import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def load_and_pad_runs(folder_path):
    runs = [pd.read_csv(f) for f in glob.glob(os.path.join(folder_path, "*.csv"))]
    max_time = max(df['timestep'].max() for df in runs)

    padded_runs = []
    for df in runs:
        last_row = df.iloc[-1]
        for t in range(df['timestep'].max() + 1, max_time + 1):
            df = pd.concat([df, pd.DataFrame([{
                'timestep': t,
                'susceptible': last_row['susceptible'],
                'infected': last_row['infected'],
                'recovered': last_row['recovered']
            }])], ignore_index=True)
        padded_runs.append(df)

    return padded_runs

def average_runs(runs):
    combined = pd.concat(runs)
    averaged = combined.groupby("timestep").mean().reset_index()
    return averaged

def plot_sir_curve(avg_df, scenario_name="Scenario"):
    plt.figure(figsize=(10, 6))
    plt.plot(avg_df['timestep'], avg_df['susceptible'], label='Susceptible')
    plt.plot(avg_df['timestep'], avg_df['infected'], label='Infected')
    plt.plot(avg_df['timestep'], avg_df['recovered'], label='Recovered')
    plt.xlabel("Timestep")
    plt.ylabel("Population Count")
    plt.title(f"Average SIR Curve: {scenario_name}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
