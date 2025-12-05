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
## 3. Launching the Application

Run the following command in the project directory:

```bash
streamlit run app.py
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
