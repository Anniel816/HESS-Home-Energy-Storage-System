# HESS Codebook

This codebook documents all variables, data structures, and simulated datasets used in the HESS Streamlit application.

---

## 1. Overview

The HESS prototype relies on simulated data because no real household energy dataset is required for demonstrating the design and user workflow. The simulation models realistic patterns of solar generation, home load, and battery changes over time.

This codebook describes:

- Variables and definitions  
- Units and ranges  
- Simulation logic  
- Intended interpretation  

---

## 2. Variables

### 2.1 User Input Variables

These values are directly controlled by the user through Streamlit widgets.

| Variable        | Type         | Unit | Description                                  | Range     |
|----------------|--------------|------|----------------------------------------------|-----------|
| `battery_level`| slider input | %    | Current battery state-of-charge              | 0–100     |
| `solar_output` | slider input | kW   | Real-time solar panel output                 | 0–10      |
| `home_load`    | slider input | kW   | Energy consumed by home appliances           | 0–8       |
| `ev_charging`  | boolean      | —    | Whether EV charging is enabled               | True/False|

---

### 2.2 Simulated Time-Series Dataset

The application generates time-series data for 24 hours (hourly resolution) for visualization.

| Variable            | Type      | Unit | Description                                                                 |
|---------------------|-----------|------|-----------------------------------------------------------------------------|
| `time`              | timestamp | hour | 24-hour range, hourly intervals ending at the current time                 |
| `Solar (kW)`        | float     | kW   | Simulated solar generation curve based on a sinusoidal daylight model      |
| `Home Load (kW)`    | float     | kW   | Randomized household load between 2–5 kW                                   |
| `Battery Level (%)` | float     | %    | Linear interpolation from an initial battery value to the current value    |

---

## 3. Simulation Logic

### 3.1 Time Vector

A 24-hour time index is generated using hourly intervals:

```python
date_range = pd.date_range(
    end=pd.Timestamp.now(),
    periods=24,
    freq="H"
)
### 3.2 Solar Generation
solar_curve = np.clip(
    np.sin(np.linspace(0, np.pi, 24)) * 8,
    0,
    None
)
### 3.3 Home Load
home_load_series = np.random.uniform(2, 5, 24)
### 3.4 Battery Level
battery_series = np.linspace(
    battery_level - 10,
    battery_level,
    24
)
### 3.5 Dataset Assembly
df = pd.DataFrame({
    "time": date_range,
    "Solar (kW)": solar_curve,
    "Home Load (kW)": home_load_series,
    "Battery Level (%)": battery_series
})
