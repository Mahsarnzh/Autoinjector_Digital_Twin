import streamlit as st
from streamlit.components.v1 import components

# Function to render the different pages
def render_page(page):
    if page == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home Page!")
    elif page == "About":
        st.title("About Page")
        st.write("This is the About Page.")
    elif page == "Contact":
        st.title("Contact Page")
        st.write("You can contact us through the Contact Page.")

# Sidebar for page selection
page = st.sidebar.selectbox("Select a Page", ["Home", "About", "Contact"])

# Render the selected page
render_page(page)
