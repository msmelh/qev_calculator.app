import streamlit as st

# Title and description
st.title("EV Charger Installation Calculator")
st.write("Use this app to calculate installation requirements based on key parameters.")

# User Inputs
panel_rating = st.selectbox("Panel Rating (A)", options=[100, 150, 200])
home_size = st.selectbox("Home Size", options=["small", "medium", "large"])
charger_load = st.selectbox("Charger Load (A)", options=[30, 40, 48])  # Multiple amp values
year_built = st.slider("Year Built", min_value=1900, max_value=2023, step=1)

# Logic to calculate recommendations
def calculate_recommendations(panel_rating, home_size, charger_load, year_built):
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

    if year_built < 1980:
        recommendations.append("Inspect wiring and panel age")
        reasons.append("Homes built before 1980 often have older wiring and panels that may need upgrading.")
    elif year_built < 2000 and panel_rating < 150:
        recommendations.append("Consider panel upgrade")
        reasons.append("Homes built before 2000 with panels under 150A may not support modern electrical loads.")

    if charger_load > 40:
        recommendations.append("Ensure panel supports high-amperage charger")
        reasons.append("Chargers requiring over 40A may need additional capacity or load management.")

    return recommendations, reasons

# Generate results
recommendations, reasons = calculate_recommendations(panel_rating, home_size, charger_load, year_built)

# Display results
st.subheader("Recommendations")
for rec in recommendations:
    st.write(f"- {rec}")

st.subheader("Reasons")
for reason in reasons:
    st.write(f"- {reason}")