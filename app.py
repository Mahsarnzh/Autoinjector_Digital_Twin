# app.py
import streamlit as st
from about import image
import pandas as pd
import matplotlib.pyplot as plt
# from about import skin_penetration_sim
from Autoinjector_Monitoring import skin_penetration_sim
from Autoinjector_Monitoring import Autoinjector_Monitoring  # Corrected import
from Autoinjector_Monitoring import skin_penetration_mon  # Corrected import
from home import generate_and_display_shap_summary_plot
from home import plot_pred_results
from about import open_webpage

def main():
    # Sidebar navigation
    pages = ["Home","about", "Autoinjector Simulation", "Autoinjector Monitoring", "Predictive Modeling"]
    page_selection = st.sidebar.radio("Go to", pages)

    # Display selected page
    if page_selection == "Home":
        st.write("# Welcome to Amgen's Digital Twin Home Page!")
        Click = st.button("Click to Open AIMOVIG® SureClick® autoinjector Instructions")
        if Click:
            open_webpage()

    elif page_selection == "Autoinjector Simulation":
        skin_penetration_sim()
    elif page_selection == "about":
        image()
    elif page_selection == "Autoinjector Monitoring":
        Autoinjector_Monitoring()
        skin_penetration_mon()
    elif page_selection ==  "Predictive Modeling":
        plot_pred_results()
        generate_and_display_shap_summary_plot()







if __name__ == "__main__":
    main()

