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
```
### 3.2 Solar Generation
Modeled using a half-sine curve to approximate daytime solar output:
```python
solar_curve = np.clip(
    np.sin(np.linspace(0, np.pi, 24)) * 8,
    0,
    None
)
```
- Values are clipped at 0 to avoid negative generation.
- Peak output is around 8 kW at midday.
- Early morning and late evening values are close to 0 kW.

### 3.3 Home Load
Home load is simulated as a random draw from a uniform distribution:
```python
home_load_series = np.random.uniform(2, 5, 24)
```
- Lower bound: 2 kW
- Upper bound: 5 kW
- Represents typical continuous household usage (lighting, appliances, HVAC).
  
### 3.4 Battery Level
Battery level is modeled as a simple linear trend over the 24-hour period, based on the current slider value:
```python
battery_series = np.linspace(
    battery_level - 10,
    battery_level,
    24
)
```
- Assumes the battery has charged by approximately 10 percentage points over the past 24 hours.
- Ensures a smooth trend suitable for visualization.

### 3.5 Dataset Assembly
All components are combined into a single DataFrame:
```python
df = pd.DataFrame({
    "time": date_range,
    "Solar (kW)": solar_curve,
    "Home Load (kW)": home_load_series,
    "Battery Level (%)": battery_series
})
```
This DataFrame is used for plotting the energy trends within the Streamlit app.

## 4. Interpretation and Assumptions

- This section explains how to interpret the simulated values and what assumptions guide the model.
- The dataset is fully simulated; it does not reflect a specific real household.
- Solar follows a natural daylight performance curve (low at dawn/dusk, peak at noon).
- Home load fluctuates reasonably to show realistic household consumption.
- Battery level changes gradually to keep trends visually meaningful.
- EV charging (ev_charging) affects recommendation logic but does not alter the simulated dataset in this prototype.
- The goal is clarity and interpretability rather than engineering precision.
## 5. Reproducibility
To ensure reproducibility, all simulations originate directly from code executed at runtime.
The dataset can be made deterministic by adding a random seed:
```python
np.random.seed(42)
```
Reproducibility notes:

- The dataset structure remains constant (24-hour, hourly resolution).
- Only the home load series is stochastic unless seeded.
- Re-running the application regenerates the dataset in the same format.
- All values derive strictly from the logic shown above — no hidden or external sources.
