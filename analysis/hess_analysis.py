import numpy as np
import pandas as pd
from datetime import datetime

def simulate_hess_data(
    battery_level: float = 65.0,
    hours: int = 24,
    seed: int = 42
) -> pd.DataFrame:
    """
    Simulate 24-hour HESS data consistent with the Streamlit prototype logic.
    
    Parameters
    ----------
    battery_level : float
        Current battery state-of-charge in percent (0–100).
    hours : int
        Number of hours to simulate (default 24).
    seed : int
        Random seed for reproducible results.
    
    Returns
    -------
    df : pd.DataFrame
        DataFrame with time, Solar (kW), Home Load (kW), Battery Level (%).
    """
    np.random.seed(seed)

    # 1. Time vector: last `hours` hours up to now
    date_range = pd.date_range(
        end=pd.Timestamp.now(),
        periods=hours,
        freq="H"
    )

    # 2. Solar generation: sinusoidal curve between 0 and ~8 kW
    solar_curve = np.clip(
        np.sin(np.linspace(0, np.pi, hours)) * 8,
        0,
        None
    )

    # 3. Home load: random between 2–5 kW
    home_load_series = np.random.uniform(2, 5, hours)

    # 4. Battery level: linear from (battery_level - 10) to battery_level
    battery_series = np.linspace(
        battery_level - 10,
        battery_level,
        hours
    )

    df = pd.DataFrame({
        "time": date_range,
        "Solar (kW)": solar_curve,
        "Home Load (kW)": home_load_series,
        "Battery Level (%)": battery_series
    })

    return df


def add_basic_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add simple analytical columns:
    - Net Load (kW)       = Home Load - Solar
    - Solar Utilization   = min(Home Load, Solar) / Solar   (0–1)
    """
    # 1. Net Load: positive = need grid/battery; negative = surplus solar
    df["Net Load (kW)"] = df["Home Load (kW)"] - df["Solar (kW)"]

    # 2. Solar Utilization: how much solar is directly used by the home
    # Avoid division by zero when Solar == 0
    utilization = []
    for solar, load in zip(df["Solar (kW)"], df["Home Load (kW)"]):
        if solar <= 0:
            utilization.append(np.nan)  # no solar, utilization undefined
        else:
            utilization.append(min(load, solar) / solar)
    df["Solar Utilization"] = utilization

    return df


def print_summary(df: pd.DataFrame) -> None:
    """
    Print a simple textual summary of the simulated day.
    """
    print("\n================ HESS Daily Summary ================")

    # 1. Basic stats
    avg_solar = df["Solar (kW)"].mean()
    avg_load = df["Home Load (kW)"].mean()
    avg_battery = df["Battery Level (%)"].mean()
    avg_net_load = df["Net Load (kW)"].mean()

    print(f"Average Solar Generation : {avg_solar:.2f} kW")
    print(f"Average Home Load        : {avg_load:.2f} kW")
    print(f"Average Battery Level    : {avg_battery:.1f} %")
    print(f"Average Net Load         : {avg_net_load:.2f} kW")

    # 2. Surplus vs deficit hours
    surplus_hours = (df["Net Load (kW)"] < 0).sum()
    deficit_hours = (df["Net Load (kW)"] > 0).sum()

    print(f"\nHours with solar surplus (Net Load < 0): {surplus_hours} / {len(df)}")
    print(f"Hours with energy deficit (Net Load > 0): {deficit_hours} / {len(df)}")

    # 3. Solar utilization stats (ignore NaN when solar = 0)
    util_mean = df["Solar Utilization"].mean(skipna=True)
    print(f"\nAverage Solar Utilization (when solar > 0): {util_mean * 100:.1f} %")

    # 4. Example: last hour conditions
    last = df.iloc[-1]
    print("\n----- Last Hour Snapshot -----")
    print(f"Time               : {last['time']}")
    print(f"Solar (kW)         : {last['Solar (kW)']:.2f}")
    print(f"Home Load (kW)     : {last['Home Load (kW)']:.2f}")
    print(f"Net Load (kW)      : {last['Net Load (kW)']:.2f}")
    print(f"Battery Level (%)  : {last['Battery Level (%)']:.1f}")
    print(f"Solar Utilization  : {last['Solar Utilization']*100:.1f} %" 
          if not np.isnan(last["Solar Utilization"]) else
          "Solar Utilization  : N/A (no solar in this hour)")

    print("====================================================\n")


def main():
    # You can change this to match your default Streamlit values
    battery_level = 65.0  # %
    hours = 24

    # 1. Simulate data
    df = simulate_hess_data(
        battery_level=battery_level,
        hours=hours,
        seed=42
    )

    # 2. Add analysis columns
    df = add_basic_analysis(df)

    # 3. Show first few rows
    print("First 5 rows of the simulated dataset with analysis:\n")
    print(df.head(), "\n")

    # 4. Print textual summary
    print_summary(df)


if __name__ == "__main__":
    main()
