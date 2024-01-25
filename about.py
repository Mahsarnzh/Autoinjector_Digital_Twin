import streamlit as st

def Autoinjector_Monitoring():
    st.title("Autoinjector Monitoring")
    st.write("This is the About Page.")


def image():

    st.title("A Digital Twin Framework for Autoinjectors")

    st.markdown("Mahsa Raeisinezhad")
    st.write("""
    \nMechanical Engineer/Data Engineer/Data Scientist 
    """)
    st.markdown("Mahsaraeesinezhad@gmail.com")
        
    autoinj = st.checkbox("## Why autoinjectors")
    if autoinj:
        st.markdown("These devices are designed to enhance convenience, patient adherence, and overall treatment experience. Companies involved in biopharmaceuticals, may explore or incorporate autoinjection technologies as part of their efforts to improve drug delivery.")
        markdown_text = """
        Even though autoinjectors are designed to enhance convenience, patient adherence, and overall treatment experience, there are unpredicted problems that can be solved through the correct control strategies provided by DTs.

        **Solution:**
        The solution is to integrate smart control strategies through digital twins, which can detect those key differences and apply the right control strategy.
        """

        # Display the markdown text
        st.markdown(markdown_text)
            
    dt = st.checkbox("### What are Digital Twins", key="dt_checkbox")
    if dt:
        markdown_text = """
        #### Digital Twins Overview

        Digital twins are virtual representations of physical objects, processes, or systems. These virtual models are created and maintained in real-time, providing a detailed and dynamic reflection of their physical counterparts. The concept of digital twins has gained prominence in various industries, including manufacturing, healthcare, construction, and more.

        **Key Points about Digital Twins:**

        1. **Virtual Representation:** Digital twins are digital replicas or models of physical entities, such as machines, buildings, or even entire systems.

        2. **Real-Time Updates:** They are continuously updated to reflect the current state of the corresponding physical object or system. This real-time synchronization enables monitoring and analysis.

        3. **Interconnected Systems:** Digital twins often involve the integration of various technologies, including the Internet of Things (IoT), sensors, data analytics, and simulation.

        4. **Applications:** Digital twins find applications in predictive maintenance, performance optimization, design simulation, monitoring, and analysis of complex systems.

        5. **Lifecycle Management:** They cover the entire lifecycle of an object or system, from design and manufacturing to operation and maintenance.

        6. **Cross-Disciplinary:** Digital twins are used in various domains, bridging disciplines like computer science, engineering, and data analytics. For example, in mechanical engineering, digital twins can represent the virtual counterpart of a physical machine, allowing for simulation and analysis.

        The concept of digital twins is evolving and holds great potential for improving efficiency, decision-making, and innovation across different industries by providing a deeper understanding and control of physical entities and processes.
        """

        # Display the markdown text
        st.markdown(markdown_text)
        b_1 = st.checkbox("## Definition:")
        if b_1:
            st.write("#### Defining a DT can be subjective. DT it is a virtual counterpart to a physical product, with data and information flowing between them through sensors.​")
            st.write("Every DT consists of:")
            st.markdown("- Physical System: Real world device that we want to replicate, monitore, or controll by its digital counterpart ")
            st.markdown(" - Digital/Virtual Counter Part: Physics of the physical system or AI models or simualtions of the physical system like ANSYS")
            st.markdown("- Set of relationships, means and connections between them to allow information exchange between the physical system and the digital counter part, such as advanced sensors or IoT sensors")
            image_path = "DT.png"
            st.image(image_path, caption='Digital Twin (DT) framework using physics of the autoinjector to simulate the fault free behavior of the autoinjector', use_column_width=True)


    image_path = "Amgen_needle.png"
    st.image(image_path, caption='Free body diagram and physics of the syringe for simulating the behavir of both tip of the needle and the syringe rubber', use_column_width=True)


def open_webpage():
    st.markdown("[Instructions for AIMOVIG® SureClick® autoinjector use(70 mg/mL)](https://www.pi.amgen.com/united_states/aimovig/aimovig_ifu_70#s1)")




if __name__ == "__main__":
    image()