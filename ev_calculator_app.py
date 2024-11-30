import streamlit as st
import pandas as pd

def installation_services_calculator_with_year(panel_rating, home_size, conduit_length, charger_load, year_built):
    recommendations = []
    reasons = []

    if home_size == "small" and panel_rating <= 100:
        recommendations.append("Main panel upgrade")
        reasons.append("Small homes with 100A panels often lack capacity for an EV charger.")
    elif home_size == "medium" and panel_rating <= 150:
        if charger_load > 30:
            recommendations.append("Load management system or main panel upgrade")
            reasons.append("Medium homes with 150A panels may need load management for higher charger loads.")
    elif home_size == "large" and panel_rating < 200:
        recommendations.append("Main panel upgrade")
        reasons.append("Large homes with panels under 200A are unlikely to support additional loads.")

    if panel_rating >= 150 and home_size in ["medium", "large"]:
        recommendations.append("Check breaker availability")
        reasons.append("If no breaker space is available, a sub-panel or load management system may be needed.")

    if conduit_length > 50:
        recommendations.append("Long conduit run installation")
        reasons.append("Conduit length over 50 feet may require additional material and labor.")
    elif conduit_length > 100:
        recommendations.append("Significant conduit run adjustment")
        reasons.append("Conduit runs over 100 feet often require specialized installation techniques.")

    if year_built < 1980:
        recommendations.append("Inspect wiring and panel age")
        reasons.append("Homes built before 1980 often have older wiring and panels that may need upgrading.")
    elif year_built < 2000 and panel_rating < 150:
        recommendations.append("Consider panel upgrade")
        reasons.append("Homes built before 2000 with panels under 150A may not support modern electrical loads.")

    if charger_load > 40:
        recommendations.append("Ensure panel supports high-amperage charger")
        reasons.append("Chargers requiring over 40A may need additional capacity or load management.")

    return {"Recommendations": recommendations, "Reasons": reasons}

# Streamlit UI
st.title("EV Charger Installation Calculator")

# User inputs
panel_rating = st.selectbox("Panel Rating (A)", options=[100, 150, 200])
home_size = st.selectbox("Home Size", options=["small", "medium", "large"])
conduit_length = st.slider("Conduit Length (ft)", min_value=0, max_value=200, step=5)
charger_load = st.slider("Charger Load (A)", min_value=20, max_value=60, step=5)
year_built = st.slider("Year Built", min_value=1900, max_value=2023, step=1)

# Calculate results
results = installation_services_calculator_with_year(panel_rating, home_size, conduit_length, charger_load, year_built)

# Display results
st.subheader("Recommendations")
for rec in results["Recommendations"]:
    st.write(f"- {rec}")

st.subheader("Reasons")
for reason in results["Reasons"]:
    st.write(f"- {reason}")