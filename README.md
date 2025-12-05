# HESS — Home Energy Storage System Dashboard  
SYSEN 5151 Final Project

HESS is an interactive UI prototype that demonstrates the user experience and workflow of a smart Home Energy Storage System app. It encompasses features like solar panel monitoring, energy storage status, EV charging management, and AI-driven energy optimization.

This repository provides all the documentation needed to use and understand the design prototype tool (Figma).

---
You can view and interact with the full HESS UI prototype here:

Figma Design File:
https://www.figma.com/design/jZbQvsk0f8iFuZgwDrQF0J/HESS?node-id=0-1

Figma Clickable Prototype:
https://www.figma.com/proto/jZbQvsk0f8iFuZgwDrQF0J/HESS?node-id=1-5307&p=f&t=Z0ZFiKPjseQgXG71-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A5307

If the prototype link does not automatically open the interactive flow, please switch to Prototype mode inside Figma.

---

## 📌 Table of Contents
1. Project Overview  
2. System Architecture  
3. Dataset Description  
4. Variable Codebook  
5. Implemented Features  
6. Usage Instructions  
7. Analytical Documentation  
8. Limitations & Future Work  
9. Repository Structure  

---

## 1. Project Overview

HESS provides homeowners with an intuitive dashboard to:

- Monitor solar generation  
- Examine home energy consumption  
- Track battery SOC  
- Determine whether EV charging is optimal  
- Understand 24-hour energy behavior through simulated data  

The prototype aligns with the original Figma design and expands functionality through a Python analysis module.


---

## 2. System Architecture

Text-based diagram:

User Inputs → Simulation Engine → 24h Dataset → Dashboard Visuals → Rule-Based Recommendations  
                                        ↘  
                                         Analytical Module (Python)

System components:

- Streamlit UI  
- Synthetic data generator  
- Altair 24-hour visualization  
- Recommendation logic  
- Analytical module (net load, utilization, SOC trends, EV feasibility)

---

## 3. Dataset Description

The project uses a fully simulated dataset for clarity, reproducibility, and privacy.

Dataset components include:

- **Solar Generation:** sinusoidal daylight curve  
- **Home Load:** random uniform between 2–5 kW  
- **Battery SOC:** linear interpolation across 24 hours  
- **EV Charging State:** boolean  

Full dataset documentation:  
👉 [docs/dataset_description.md](docs/dataset_description.md)

---

## 4. Variable Codebook

The complete variable list is provided in:  
👉 [docs/codebook.md](docs/codebook.md)

Core variables:

| Variable | Type | Description |
|---------|------|-------------|
| battery_level | slider | Battery SOC (%) |
| solar_output | slider | Real-time solar generation (kW) |
| home_load | slider | Household demand (kW) |
| ev_charging | toggle | EV charging enabled/disabled |
| Solar (kW) | simulated | Hourly solar generation |
| Home Load (kW) | simulated | Hourly household load |
| Battery Level (%) | simulated | Hourly SOC |

---

## 5. Implemented Features

### ✔ Dashboard UI
- Battery SOC progress bar  
- Real-time solar and load indicators  
- EV charging UI (fixed 7.2 kW)  
- 24-hour solar vs. load trend chart  

### ✔ Energy Analysis (Python)
A dedicated analytical module performs:

- Net Load calculation  
- Solar Utilization calculation  
- SOC trend interpretation  
- EV charging feasibility assessment  

Documentation:  
👉 [docs/HESS_Analytical_Documentation.md](docs/HESS_Analytical_Documentation.md)  

Python script:  
👉 [analysis/hess_analysis.py](analysis/hess_analysis.py)

---

## 6. Usage Instructions

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Run the dashboard:
```bash
streamlit run app.py
```

## 7. Analytical Documentation

All analytical work required by the rubric is detailed here:

👉 [docs/HESS_Analytical_Documentation.md](docs/HESS_Analytical_Documentation.md)

Includes:

- Analytical methods (plain text formulas)  
- Computed numerical results  
- Interpretation of outcomes  
- Limitations and assumptions  
- Future analytical extensions  

---

## 8. Limitations & Future Work

### Current Limitations
- Solar simulation is idealized  
- Home load is randomized  
- Battery SOC uses a linear model  
- EV charging logic is rule-based  
- No weather, pricing, or real hardware integration  

### Future Expansion
- Solar and load forecasting (LSTM, Prophet, SARIMA)  
- MILP battery optimization  
- Smart EV charging scheduling  
- API-based real-time data ingestion (inverter, smart meter)  

---

## 9. Repository Structure

HESS/
├── app.py
├── analysis/
│ └── hess_analysis.py
├── docs/
│ ├── analysis_documentation.md
│ ├── codebook.md
│ ├── dataset_description.md
│ ├── development_plan_alignment.md
│ ├── usage_instructions.md
│ └── user_persona_use_case.md
└── README.md