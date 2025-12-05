# Dataset Description for HESS Prototype

The HESS prototype does not rely on external datasets. Instead, it uses internally generated simulated data to illustrate how a home energy system behaves over time.

This document describes:

- Why simulation is used  
- How values are generated  
- What each dataset component represents  

---

## Why Simulated Data?

- No real household data is required for design demonstration  
- Supports meaningful visualization without privacy concerns  
- Behaves similarly to real solar and load profiles  
- Ensures full reproducibility  

---

## Data Components

### 1. **Solar Generation**
- Simulated using a sinusoidal curve  
- Peaks at midday  
- Represents typical solar panel output behavior

### 2. **Home Load**
- Randomized between 2–5 kW  
- Represents lights, appliances, HVAC, etc.

### 3. **Battery Level**
- Controlled by user input  
- Interpolated across 24 hours  
- Represents slow charging trend

### 4. **EV Charging**
- Simple boolean input  
- Affects AI recommendations (but not data generation)

---

## Summary

This simulation accurately reflects realistic energy flows and provides a strong foundation for demonstrating:

- Dashboards  
- Line charts  
- Forecast-like patterns  
- Recommendations  

It is appropriate for the educational and prototype-focused nature of this project.
