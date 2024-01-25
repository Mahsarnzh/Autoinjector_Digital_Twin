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
        python_code = """
        def build_model(self):
            return MLPRegressor(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=10, random_state=42)"""
        st.code(python_code, language='python')
        st.write(" The given code snippet is creating an instance of an artificial neural network (ANN) model using scikit-learn's MLPRegressor class. MLP stands for Multi-Layer Perceptron, which is a type of artificial neural network with multiple layers (input layer, hidden layers, and output layer).")
        
        generate_and_display_shap_summary_plot()
        st.markdown("""
        ### SHAP: Explaining Machine Learning Models

        SHAP (SHapley Additive exPlanations) is a popular Python library for explaining the output of machine learning models. It provides a unified measure of feature importance that can be applied to various model types, including tree-based models, linear models, support vector machines, and more.

        **Key features of SHAP:**

        - **Interpretability:** SHAP values provide a way to interpret the impact of each feature on the model's output for a specific prediction. It helps to understand the contribution of each feature to the final prediction.

        - **Shapley Values:** SHAP values are based on Shapley values from cooperative game theory. They provide a fair way to distribute the contribution of each feature to the prediction across all possible combinations of features.

        - **Global and Local Interpretability:** SHAP can be used to explain individual predictions (local interpretability) as well as understand the overall behavior of the model (global interpretability).

        - **Model-Agnostic:** SHAP is model-agnostic, meaning it can be applied to any machine learning model, making it versatile and applicable to a wide range of scenarios.

        - **Visualization:** SHAP provides tools for visualizing and interpreting the impact of features on predictions. Common visualizations include summary plots, force plots, and dependence plots.

        To use SHAP, you typically follow these steps:

        1. Train a machine learning model.
        2. Use SHAP to explain the model's predictions for specific instances.
        """)
        python_code_1 = """
        !pip install shap 
        import shap

        # Create a function that takes input features and returns model predictions
        def predict_external_force(inputs):
            return model_external_force.predict(inputs)

        def predict_needle_angle(inputs):
            return model_needle_angle.predict(inputs)
        explainer_external_force = shap.Explainer(predict_external_force, X_train[:10])
        shap_values_external_force = explainer_external_force.shap_values(X_train[:10])

        shap.summary_plot(shap_values_external_force, X_train[:10], max_display=10)
        
        """
        st.code(python_code_1, language='python')

        st.write("""The process described lacks real-time sensor data, which is essential for it to qualify as a Digital Twin (DT) technology. Instead, synthetic data has been employed to simulate real-time behavior, substituting actual sensor measurements (Noisy Measurements).""")
    
    
if __name__ == "__main__":
    main()

