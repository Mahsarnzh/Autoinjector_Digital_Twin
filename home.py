import streamlit as st
import numpy as np
import shap
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

class NeuralNetworkRegressor:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.imputer_numeric = SimpleImputer(strategy='mean')
        self.imputer_non_numeric = SimpleImputer(strategy='constant', fill_value="0")

    def preprocess_data(self, df):
        df.fillna(0, inplace=True)

        X = df.drop(['External Force', 'Needle Angle', 'Injection Type'], axis=1)
        y_external_force = df['External Force'].values
        y_needle_angle = df['Needle Angle'].values

        X_train, X_test, y_external_force_train, y_external_force_test, y_needle_angle_train, y_needle_angle_test = train_test_split(
            X, y_external_force, y_needle_angle, test_size=0.2, random_state=42
        )

        X_train_scaled = X_train
        X_test_scaled = X_test

        return X_train_scaled, X_test_scaled, y_external_force_train, y_external_force_test, y_needle_angle_train, y_needle_angle_test

    def build_model(self):
        return MLPRegressor(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=10, random_state=42)

    def train_and_evaluate(self, X_train_scaled, X_test_scaled, y_train, y_test):
        self.model.fit(X_train_scaled, y_train)
        y_pred = self.model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')

    def train_external_force_model(self, X_train_scaled, X_test_scaled, y_external_force_train, y_external_force_test):
        self.model = self.build_model()
        self.train_and_evaluate(X_train_scaled, X_test_scaled, y_external_force_train, y_external_force_test)

    def train_needle_angle_model(self, X_train_scaled, X_test_scaled, y_needle_angle_train, y_needle_angle_test):
        self.model = self.build_model()
        self.train_and_evaluate(X_train_scaled, X_test_scaled, y_needle_angle_train, y_needle_angle_test)

# Usage
df = pd.read_csv('simulation_results_9.csv')
regressor = NeuralNetworkRegressor()

# Preprocess the data and train the external force model
X_train_scaled, X_test_scaled, y_external_force_train, y_external_force_test, _, _ = regressor.preprocess_data(df)
regressor.train_external_force_model(X_train_scaled, X_test_scaled, y_external_force_train, y_external_force_test)
y_external_force_pred = regressor.model.predict(X_test_scaled)


def plot_pred_results():
    st.subheader("Prediction vs unseen (test) data")
    
    # Create a Matplotlib figure explicitly
    fig, ax = plt.subplots(figsize=(10, 6))

    # Generate the plot
    ax.plot(y_external_force_test[0:100], color='blue', label='Real External Force')
    ax.plot(y_external_force_pred[0:100], color='red', label='Predicted External Force')
    ax.set_title('Predictions vs. Real Data for External Force')
    ax.set_xlabel('time')
    ax.set_ylabel('Predicted External Force')
    ax.legend()

    # Display the Matplotlib plot using Streamlit
    st.pyplot(fig)



# Create a function that takes input features and returns model predictions
def predict_external_force(inputs):
    return regressor.model.predict(inputs)

def generate_and_display_shap_summary_plot():
    st.subheader("SHAP Summary Plot for External Force")
    explainer = shap.Explainer(predict_external_force, X_train_scaled[:10])
    shap_values = explainer.shap_values(X_train_scaled[:10])
    features = X_train_scaled[:10]
    max_display =  max_display=10
    # Create a Matplotlib figure explicitly
    fig, ax = plt.subplots()

    # Generate the SHAP summary plot
    shap.summary_plot(shap_values, features, max_display=max_display, show=False)

    # Display the Matplotlib plot using Streamlit
    st.pyplot(fig)
