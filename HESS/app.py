import streamlit as st
import pandas as pd
import numpy as np
import datetime
import altair as alt

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="HESS - Home Energy Storage System",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 HESS — Home Energy Storage System Dashboard")
st.write("A visual prototype simulation based on the Figma UI design.")

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
st.sidebar.title("⚙️ System Controls")

battery_level = st.sidebar.slider("Battery Level (%)", 0, 100, 65)
ev_charging = st.sidebar.toggle("EV Charging Enabled", value=True)
solar_output = st.sidebar.slider("Solar Output (kW)", 0.0, 10.0, 4.5)
home_load = st.sidebar.slider("Home Load (kW)", 0.0, 8.0, 3.2)

# ------------------------------------------------------
# LAYOUT
# ------------------------------------------------------
col1, col2, col3 = st.columns(3)

# Battery Panel
with col1:
    st.subheader("🔋 Battery Storage")
    st.metric("Current Charge", f"{battery_level} %")
    st.progress(battery_level)

# Solar Panel
with col2:
    st.subheader("☀️ Solar Generation")
    st.metric("Solar Output", f"{solar_output} kW")

# EV Charging
with col3:
    st.subheader("🚗 EV Charging")
    status = "Enabled" if ev_charging else "Disabled"
    st.metric("Status", status)
    st.write("Charging Rate: **7.2 kW**" if ev_charging else "Charging paused")

# ------------------------------------------------------
# CHART SECTION
# ------------------------------------------------------
st.subheader("📈 Energy Trends (Demo Simulation)")

date_range = pd.date_range(end=pd.Timestamp.now(), periods=24, freq="H")

df = pd.DataFrame({
    "time": date_range,
    "Solar (kW)": np.clip(np.sin(np.linspace(0, 3.14, 24)) * 8, 0, None),
    "Home Load (kW)": np.random.uniform(2, 5, 24),
    "Battery Level (%)": np.linspace(battery_level - 10, battery_level, 24)
})

chart = alt.Chart(df).transform_fold(
    ["Solar (kW)", "Home Load (kW)"],
    as_=["Type", "kW"]
).mark_line().encode(
    x="time:T",
    y="kW:Q",
    color="Type:N"
).properties(height=300)

st.altair_chart(chart, use_container_width=True)

# ------------------------------------------------------
# AI Recommendations Section
# ------------------------------------------------------
st.subheader("🤖 AI Optimization Recommendations")

if solar_output > home_load:
    st.success("You are generating more power than consuming. Consider charging your EV or storing energy.")
else:
    st.warning("Your home load exceeds solar generation. Consider reducing appliance usage or using stored battery power.")

if battery_level < 20:
    st.error("Battery low. Avoid scheduling EV charging until battery exceeds 30%.")
