# HESS Usage Instructions

This document provides step-by-step instructions for installing, launching, and using the HESS (Home Energy Storage System) Streamlit tool.

---

## 1. Prerequisites

Before running the tool, please ensure:

- Python **3.8 or higher** is installed  
- `pip` is available in your environment  
- You have cloned or downloaded the HESS GitHub repository

---

## 2. Installation

1. **Open a terminal** (Command Prompt, PowerShell, or Terminal on macOS).

2. **Navigate to the project folder** (replace the path with your own):

```bash
cd path/to/HESS
```
## 3. Simulation Logic

---

### 3.1 Time Vector
The tool generates a 24-hour timestamp sequence (hourly resolution):

```python
date_range = pd.date_range(
    end=pd.Timestamp.now(),
    periods=24,
    freq="H"
)
```
### 3.2 Solar Generation
Simulated using a sinusoidal daylight curve:
```python
solar_curve = np.clip(
    np.sin(np.linspace(0, np.pi, 24)) * 8,
    0,
    None
)
```
- Mimics sunrise → midday peak → sunset
- Peak output ~8 kW
- Negative values clipped to 0

### 3.3 Home Load
Simulated as a uniform random series representing household appliance usage:
```python
home_load_series = np.random.uniform(2, 5, 24)
```
- Values between 2–5 kW
- Represents typical residential energy consumption
- Introduces realistic variability
### 3.4 Battery Level
Simulated using linear interpolation:
```python
battery_series = np.linspace(
    battery_level - 10,
    battery_level,
    24
)
```
- Models slow charging behavior
- Produces a smooth and easy-to-interpret trend
- Final level equals user-selected battery_level
### 3.5 Dataset Assembly
The final 24-hour dataset is constructed as follows:
```python
df = pd.DataFrame({
    "time": date_range,
    "Solar (kW)": solar_curve,
    "Home Load (kW)": home_load_series,
    "Battery Level (%)": battery_series
})
```
— Dataset used for visualization
- Recomputed on every app run
-Consistent structure for analysis and plotting

## 4. Main Interface Overview

The HESS dashboard includes:

- Sidebar controls for system inputs  
- Battery, Solar, and EV status panels  
- A 24-hour simulated energy trends chart  
- An AI recommendation section providing optimization suggestions  

All elements update in real time based on user selections.

---

## 5. Using the Sidebar Controls

### 5.1 Battery Level (%)
- Adjust using the slider in the sidebar  
- Range: 0–100  
- Updates the battery metric and affects the simulated battery trend

### 5.2 Solar Output (kW)
- Slider that sets real-time solar generation  
- Range: 0–10 kW  
- Changes solar metrics and influences AI logic  

### 5.3 Home Load (kW)
- Slider representing current household consumption  
- Range: 0–8 kW  
- Used to determine balance between solar generation and usage  

### 5.4 EV Charging
- Toggle switch to simulate EV charging status  
- Affects EV metric and downstream recommendations  

---

## 6. Dashboard Metrics

The dashboard displays three primary status panels:

### Battery Storage
- Shows current battery percentage  
- Includes a visual progress bar  

### Solar Generation
- Shows real-time solar output in kW  

### EV Charging Status
- Displays whether EV charging is enabled  
- Shows sample charging rate when active  

These metrics provide at-a-glance system status.

---

## 7. Energy Trends Chart

The 24-hour chart visualizes simulated trends:

- Solar (kW)  
- Home Load (kW)  
- Battery Level (%)  

Chart features:

- X-axis: hourly timestamps  
- Y-axis: kW or % values  
- Automatically refreshes based on user inputs  

Used to help understand daily consumption and generation patterns.

---

## 8. AI Optimization Recommendations

The system provides rule-based recommendations based on:

- Solar output  
- Home load  
- Battery level  
- EV charging state  

Example outputs:

- When solar > load:  
  *“Excess solar energy available. Consider charging your EV now.”*  

- When battery is low:  
  *“Battery low. Delay EV charging until levels increase.”*  

- When load is high:  
  *“High home usage detected. Reduce non-essential load if possible.”*  

Recommendations update dynamically as controls change.

---

## 9. Typical Usage Workflow

1. Set the battery level slider  
2. Adjust solar output  
3. Adjust home load  
4. Toggle EV charging on/off  
5. Observe updated metrics  
6. Review AI recommendations  
7. Examine 24-hour trend chart for insights  

This flow simulates real energy management behavior.

---

## 10. Resetting and Restarting

To restart the application:

```bash
Ctrl + C   # stop Streamlit in terminal
streamlit run app.py
```

