import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

def about_page():
    st.title("About Page")
    st.write("This is the About Page.")



def update_global_parameters():
    global tissue_coeficient_friction, needle_diameter, applied_force, humidity, temperature, bending_force_max, bending_force_min, injection_type
    tissue_coeficient_friction = st.slider("Softener tissue coeficient friction", 0.0, 100.0, 0.33, 0.01)
    needle_diameter = st.slider("Needle Diameter (mm)", 0.01, 1e2, 10.0)
    applied_force = st.slider("Applied Force (N)", 19.0, 100.0, 50.0, 1.0)
    humidity = st.slider("Humidity", 0.0, 1.0, 0.5, 0.01)
    temperature = st.slider("Temperature (°C)", -10, 90, 30, 1)
    bending_force_max = st.slider("maximum allowable needle's bending force", 10.0, 10.9, step=0.1)
    bending_force_min = st.slider("Minimum allowable needle's bending force", bending_force_max - 0.2 , bending_force_max - 0.1, 0.2)
    options = ["Intramuscular", "Subcutaneous", "Intradermal"]
    injection_type =  st.radio("Select injection type:", options)



update_global_parameters()

def skin_penetration_sim():
    global temperature

    st.title("Syringe Skin Penetration Simulation")    


    # User input for simulation parameters

    update_global_parameters()
    # Simulate syringe skin penetration
    time_points, penetration_depths, velocities, needle_angle_rad_avg_ , vel_rubbs, disp_rubs = simulate_syringe_skin_penetration(
        external_force = applied_force , humidity = humidity, temperature = temperature, needle_length=0.05 , tissue_coeficient_friction = tissue_coeficient_friction, needle_diameter = needle_diameter,
        time_step=0.001, total_time=0.03, fluid_mass=0.08, bending_force_max= bending_force_max, injection_type = injection_type)
    
    # Plotting
    st.pyplot(plot_simulation_results(time_points, penetration_depths, "Penetration Depth", "m"))
    st.pyplot(plot_simulation_results(time_points, velocities, "velocity of Needle","m/s"))
    st.pyplot(plot_simulation_results(time_points, radians_to_degree(needle_angle_rad_avg_), "Allowable Needle Angle", "degree"))
    st.pyplot(plot_simulation_results(time_points, disp_rubs, "Syringe Rubber Displacement", "m"))
    st.pyplot(plot_simulation_results(time_points, vel_rubbs, "Syringe Rubber Velocity", "m/s"))




def skin_penetration_mon():
    global temperature

    st.title("Syringe Skin Penetration Monitoring")    


    # User input for simulation parameters

    # update_global_parameters()
    # Simulate syringe skin penetration
    time_points, penetration_depths, velocities, needle_angle_rad_avg_ , vel_rubbs, disp_rubs = simulate_syringe_skin_penetration(
        external_force = applied_force , humidity = humidity, temperature = temperature, needle_length=0.05 , tissue_coeficient_friction = tissue_coeficient_friction, needle_diameter = needle_diameter,
        time_step=0.001, total_time=0.03, fluid_mass=0.08, bending_force_max= bending_force_max, injection_type = injection_type)
    
    noisy_penetration_depths = add_noise_to_timeseries(penetration_depths, noise_factor=0.001)
    noisy_velocities = add_noise_to_timeseries(velocities, noise_factor=0.07)
    noisy_needle_angle_rad_avg_ = add_noise_to_timeseries(needle_angle_rad_avg_, noise_factor=0.001)
    noisy_disp_rubs = add_noise_to_timeseries(disp_rubs, noise_factor=0.001)
    noisy_vel_rubbs = add_noise_to_timeseries(vel_rubbs, noise_factor=1)


    # Plotting
    st.pyplot(plot_simulation_results_noisy(time_points, penetration_depths, noisy_penetration_depths, "Penetration Depth", "Noisy Penetration Depth", "m"))
    st.pyplot(plot_simulation_results_noisy(time_points, velocities, noisy_velocities, "velocity of Needle","Noisy velocity of Needle","m/s"))
    st.pyplot(plot_simulation_results_noisy(time_points, radians_to_degree(needle_angle_rad_avg_), radians_to_degree(noisy_needle_angle_rad_avg_),  " Needle Angle", "Nosiy Needle Angle", "degree"))
    st.pyplot(plot_simulation_results_noisy(time_points, disp_rubs, noisy_disp_rubs, "Syringe Rubber Displacement", "Noisy Syringe Rubber Displacement","m"))
    st.pyplot(plot_simulation_results_noisy(time_points, vel_rubbs, noisy_vel_rubbs, "Syringe Rubber Velocity","Noisy Syringe Rubber Velocity", "m/s"))






def plot_simulation_results_noisy(time_points, var1, var2, label, label_2, unit):
    plt.figure(figsize=(8, 6))
    plt.plot(time_points[:len(var1)], var1, label=label)
    plt.plot(time_points[:len(var2)], var2, 'red', label=label_2)
    plt.title('Syringe Skin Penetration with Multiple Forces')
    plt.xlabel('Time (s)')
    plt.ylabel(f'{label}({unit})')
    plt.legend()
    return plt



def plot_simulation_results(time_points, variable, label, unit):
    plt.figure(figsize=(8, 6))
    plt.plot(time_points[:len(variable)], variable, label= label)
    plt.title('Syringe Skin Penetration with Multiple Forces')
    plt.xlabel('Time (s)')
    plt.ylabel(f'{label} ({unit})')
    plt.legend()
    return plt


def calculate_friction_coefficient(tissue_coeficient_friction, needle_diameter):
    # Given values
    ffi = 0.022  # Friction force per unit length (N/mm) for the specified PVC
    needle_diameter = needle_diameter* 1e-3
    P = 3.14 * needle_diameter  # Needle perimeter

    # Shear stress on the needle surface
    sigma_fi = ffi / P

    # Tissue properties
    elastic_modulus_tissue = 21.3  # Elastic modulus of tissue (kPa)
    poisson_ratio_tissue = 0.45  # Poisson's ratio of tissue

    # Normal stress on the needle surface
    sigma_ni = elastic_modulus_tissue / (1 - poisson_ratio_tissue)

    # Friction coefficient
    friction_coefficient = sigma_fi / sigma_ni

    return friction_coefficient




def simulate_syringe_skin_penetration(
    external_force, humidity, temperature, needle_length=0.05, tissue_coeficient_friction = 0.33, needle_diameter = 5e-3,
    time_step=0.001, total_time=0.03, fluid_mass=0.08, bending_force_max=10.98, injection_type = "Intramuscular"
):
    # Constants
    needle_diameter = needle_diameter*1e-2
    needle_area = 1e-6  # Cross-sectional area of the needle (m^2)
    base_skin_resistance = 500  # Base skin resistance to penetration (N/m)
    temperature_factor = 1.0 + 0.01 * (temperature - 25)  # Linear temperature effect (adjust as needed)
    syringe_area = 0.0001  # Cross-sectional area of the syringe needle (m^2)
    fluid_pressure_remaining = 127323.95  # Fluid pressure inside the syringe (Pa)
    friction_coefficient = 0.2  # Friction coefficient between syringe walls and rubber
    gravity = 9.81  # Acceleration due to gravity (m/s^2)
    empty_syringe_mass = 0.08
    rubber_mass = 0.2 * empty_syringe_mass
    fluid_remaining = syringe_area * needle_length  # Initial fluid remaining
    syringe_mass = fluid_mass + empty_syringe_mass
    fluid_density = fluid_mass / fluid_remaining


    # Variables
    time_points = np.arange(0, total_time, time_step)
    displacement = 0  # Initial displacement
    velocity = 0  # Initial velocity
    vel_rubber = 0  # Initial rubber velocity
    disp_rub = 0

    # Lists to store data for plotting
    penetration_depths = []
    velocities = []
    needle_angle_rad_ = []
    vel_rubbs = []
    disp_rubs = []
    # Simulation loop
    for time in time_points:
        penetration_depths.append(displacement)
        velocities.append(velocity)
        vel_rubbs.append(vel_rubber)
        disp_rubs.append(disp_rub)
        fluid_force = fluid_pressure_remaining * syringe_area  # Force due to fluid pressure
        friction_force = friction_coefficient * vel_rubber  # Friction force
        gravity_force = syringe_mass * gravity  # Force due to gravity
        
        # Net force
        net_syringe_force = external_force - fluid_force - friction_force + gravity_force


        acc_rubber = net_syringe_force / rubber_mass
        vel_rubber -= acc_rubber * time_step
        disp_rub += vel_rubber * time_step

        # Modified skin resistance based on humidity and temperature
        skin_resistance = base_skin_resistance * humidity * temperature_factor  # approximate: for more accurate results use Ogden material model
        needle_angle_rad = np.arccos(bending_force_max / net_syringe_force)
        bending_force_avg = gravity_force * np.cos(needle_angle_rad)
        
        # Calculate friction coefficient
        mu = calculate_friction_coefficient(tissue_coeficient_friction, needle_diameter)

        indentation_force = net_syringe_force 
        cutting_force = skin_resistance * 3.14 * (needle_diameter**2)  # Needle perimeter
        friction_force_skin = mu * velocity  # Example friction force

        # Net force
        net_force = indentation_force - (cutting_force + friction_force_skin)
            
        # Acceleration is needles acc
        acceleration = net_force / syringe_mass
        # Update velocity and displacement using numerical integration (Euler's method)
        # This vel is needle's vel
        velocity -= acceleration * time_step
        displacement += velocity * time_step # this disp is needles
        needle_angle_rad_.append(needle_angle_rad)
        fluid_pressure_remaining -= fluid_density * gravity * disp_rub
        fluid_remaining -= syringe_area * disp_rub

        if injection_type == "Intramuscular":
          max_needle_penetration = 0.04

        if injection_type == "Subcutaneous":
          max_needle_penetration = 0.02

        elif injection_type == "Intradermal":
          max_needle_penetration = 0.003 

        if abs(displacement) >= max_needle_penetration or fluid_remaining <= 0 or abs(disp_rub) >= needle_length:
            velocity = 0  # Needle has stopped, set velocity to zero
            vel_rubber = 0
            acceleration = 0
            acc_rubber = 0
            fluid_remaining = 0
            fluid_pressure_remaining = 0
            disp_rub = - needle_length
            displacement = -max_needle_penetration 
        # Store data for plotting
        if net_force <=0:
            velocity = 0  # Needle has stopped, set velocity to zero
            vel_rubber = 0
            acceleration = 0
            acc_rubber = 0
            fluid_remaining = 0
            fluid_pressure_remaining = 0
            disp_rub = 0
            displacement = 0

        # print(fluid_pressure_remaining)
        fluid_mass = fluid_density * fluid_remaining

    return time_points, penetration_depths, velocities, needle_angle_rad_, vel_rubbs, disp_rubs


def add_noise_to_timeseries(data, noise_factor=0.01):
    noise = np.random.normal(0, noise_factor, len(data))
    noisy_data = data + noise
    return noisy_data



def radians_to_degree(needle_angle_rad_avg_):
    return [math.degrees(deg) for deg in needle_angle_rad_avg_]






def Autoinjector_Monitoring():
    st.title("Autoinjector Monitoring")
    st.write("This is the About Page.")

class AutoinjectorAlarm:
    def __init__(self, temperature_threshold, temperature_threshold_heat = 50, exposed_to_sunlight=False,
                 shaken=False, cap_removed=True, expired=False):
        self.temperature_threshold = temperature_threshold
        self.temperature_threshold_heat = temperature_threshold_heat
        self.exposed_to_sunlight = exposed_to_sunlight
        self.shaken = shaken
        self.cap_removed = cap_removed
        self.expired = expired

    def check_temperature(self, current_temperature):
        if current_temperature > self.temperature_threshold:
            st.warning("Alarm: Temperature exceeds the threshold!")

    def check_exposure_to_heat(self, current_temperature):
        if current_temperature > self.temperature_threshold_heat:
            st.warning("Alarm: Exposed to heat source!")

    def check_exposure_to_sunlight(self):
        if self.exposed_to_sunlight:
            st.warning("Alarm: Exposed to sunlight!")

    def check_shaking(self, selected_option):
        if selected_option == "Shaking Detected":
            st.warning("Shaking has been detected. Take appropriate action.")
        elif selected_option == "Shaking Not Detected":
            st.warning("No shaking detected. Everything is fine.")

    def check_cap_removal(self):
        if self.cap_removed:
            st.warning("Alarm: Cap has been removed!")

    def check_expiration(self):
        if self.expired:
            st.warning("Alarm: Autoinjector has expired!")


def Autoinjector_Monitoring():
    st.title("Autoinjector Monitoring")

    # Receive user input for temperature and checkboxes
    current_temperature = temperature
    exposed_to_heat = st.checkbox("Exposed to Heat")
    exposed_to_sunlight = st.checkbox("Exposed to Sunlight")

    options = ["Shaking Not Detectedg", "Shaking Detected"]
    shaken = st.radio("Select Shaking Status:", options)

    cap_removed = st.checkbox("Cap Removed")
    expired = st.checkbox("Autoinjector Expired", True)

    # Create an instance of AutoinjectorAlarm
    autoinjector_alarm = AutoinjectorAlarm(
        temperature_threshold=25,
        temperature_threshold_heat = 60,
        exposed_to_sunlight=exposed_to_sunlight,
        shaken=shaken,
        cap_removed=cap_removed,
        expired=expired
    )

    # Display alarm messages
    autoinjector_alarm.check_temperature(current_temperature)
    st.write("Current temperature is:", current_temperature)
    autoinjector_alarm.check_exposure_to_heat(current_temperature)
    autoinjector_alarm.check_exposure_to_sunlight()
    autoinjector_alarm.check_shaking(shaken)
    autoinjector_alarm.check_cap_removal()
    autoinjector_alarm.check_expiration()


