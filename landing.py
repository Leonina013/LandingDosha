import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Dosha Prediction App", page_icon="🌿")

# Define the app title and description
st.title("Discover Your Dosha")
st.write("Welcome to the Dosha Prediction App, your guide to Ayurvedic wellness!")

# Dosha descriptions
st.header("What are Vata, Pitta, and Kapha Doshas?")
st.markdown(
    "In Ayurveda, the ancient science of holistic healing, it is believed that everyone is a unique combination of three doshas:"
)

# Display dosha images and descriptions
columns = st.columns(3)
with columns[0]:
    st.image("https://drive.google.com/file/d/1VGEipz8f0SRr6OI2r-lsQAeddK4E_W8p/view?usp=sharing", caption="Vata Dosha", use_container_width=True)
    st.write("Vata Dosha")
    st.write(
        "Vata is associated with the elements of air and ether (space). It represents energy, movement, and change. People with a predominant Vata dosha are creative, quick-thinking, and adaptable.")
    
with columns[1]:
    st.image("https://drive.google.com/file/d/1VGEipz8f0SRr6OI2r-lsQAeddK4E_W8p/view?usp=sharing", caption="Pitta Dosha", use_container_width=True)
    st.write("Pitta Dosha")
    st.write(
        "Pitta is linked to the elements of fire and water. It governs metabolism, digestion, and transformation. People with a predominant Pitta dosha tend to be determined, intelligent, and passionate.")
    
with columns[2]:
    st.image("https://drive.google.com/file/d/1VGEipz8f0SRr6OI2r-lsQAeddK4E_W8p/view?usp=sharing", caption="Kapha Dosha", use_container_width=True)
    st.write("Kapha Dosha")
    st.write(
        "Kapha corresponds to the elements of earth and water. It provides stability and structure, leading to qualities of calmness, patience, and nurturing.")

# CTA (Call to Action)
st.header("Ready to Discover Your Dosha?")
st.write("Get started with our Dosha assessment and prediction. Click the button below to begin!")

# Button to start assessment
if st.button("Start Assessment"):
    st.write("Redirect to the Dosha assessment page here")

# Disclaimer
st.markdown("Please note that the Dosha Prediction App is for informational purposes only and should not replace professional advice from an Ayurvedic practitioner.")

# Footer
st.write("© 2023 Dosha Prediction App. All rights reserved.")
