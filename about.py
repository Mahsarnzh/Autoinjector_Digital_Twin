import streamlit as st

def Autoinjector_Monitoring():
    st.title("Autoinjector Monitoring")
    st.write("This is the About Page.")


def image():
    # st.title("An Innovative Approach to Incorporate Connectivity Features into Autoinjectors")
    st.title("A Digital Twin Framework for Amgen's Autoinjectors")

    st.markdown("Mahsa Raeisinezhad")
    st.write("""
    \nMechanical Engineer/Data Engineer 
    """)
    st.markdown("Mahsaraeesinezhad@gmail.com")
        
    autoinj = st.checkbox("## Why autoinjectors")
    if autoinj:
        st.markdown("#### These devices are designed to enhance convenience, patient adherence, and overall treatment experience. Companies involved in biopharmaceuticals, including Amgen, may explore or incorporate autoinjection technologies as part of their efforts to improve drug delivery.")
    
    dt = st.checkbox("### What are Digital Twins", key="dt_checkbox")
    if dt:
        st.markdown("#### Defining a Digital Twin (DT) can be subjective Digital Twins are where the two fields of Computer Science and Mechanical Engineering meet, ")
        b_1 = st.checkbox("## Definition:")
        if b_1:
            st.write("#### DT it is a virtual counterpart to a physical product, with data and information flowing between them through IoT devices.​")
            st.write("Every DT consists of:")
            st.markdown(" - Digital/Virtual realm")
            st.markdown("- Physical counterpart")
            st.markdown("- Set of relationships, means and connections between them")
            # st.markdown("- There should be means for maintaining the relationships between the Physical counterpart and Digital/Virtual realm ​")

        b_2 = st.checkbox("## DT in pharmecuetical industry:")
        if b_2:
            st.write("#### Gerresheimer is pioneering the use of digital twin technology in the pharmaceutical supply chain to enhance safety, traceability, and quality control. By creating virtual replicas of physical assets like syringes, the company aims to securely trace the entire lifecycle of products, combat counterfeiting, and improve logistics. The benefits include improved quality, easier access to certifications, and faster identification of drugs. The application of digital twin technology is exemplified in the manufacturing of prefilled syringes, showcasing its potential in delivering high-quality medications and preventing mix-upsy")
            image_path = "Amgen_dt.jpeg"
            st.image(image_path, caption='“The benefits of digital twin technology include quality improvements throughout the supply chain and easy access to certifications issued at various stages of the process.”')
            st.write('https://www.ondrugdelivery.com/digital-twin-in-the-pharmaceutical-supply-chain/', use_column_width=True)



    image_path = "Amgen_needle.png"
    st.image(image_path, caption='Your Image Caption', use_column_width=True)


def open_webpage():
    st.markdown("[Instructions for AIMOVIG® SureClick® autoinjector use(70 mg/mL)](https://www.pi.amgen.com/united_states/aimovig/aimovig_ifu_70#s1)")

    # Display a button to open the webpage
Click = st.button("Click to Open Webpage")
if Click:
    open_webpage()



if __name__ == "__main__":
    image()