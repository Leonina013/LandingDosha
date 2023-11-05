import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/DU3tef0.jpg");
             background-attachment: fixed;
             
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


# Set page title and icon

st.title("Discover Your Dosha")
# Define the app title and description
st.image("https://i.imgur.com/ehvfiUX.png")  # Add the image here

st.write("Welcome to the Dosha Prediction App, your guide to Ayurvedic wellness!")

# Dosha descriptions
st.header("What are Vata, Pitta, and Kapha Doshas?")
st.markdown(
    "Ayurvedic wisdom reveres you as a celestial marvel, a miniature reflection of Mother Nature herself, meticulously crafted from the quintessential elements of the cosmos: ether, air, fire, water, and earth. These primordial elements elegantly converge in harmonious pairs to give birth to what is known as the tri-dosha – the three fundamental principles of energy that underpin the tapestry of life and existence. Each elemental duet boasts its distinct attributes and natural rhythms."
)

# Create columns for the dosha descriptions and images
col1, col2, col3 = st.columns(3)

# Set the same image dimensions for all images
image_width = 200  # Adjust the width as needed

# Vata Dosha
with col1:
    st.image("https://i.imgur.com/lzvGIUW.png", caption="Vata Dosha", width=image_width)
    st.write(
        "Vata is associated with the elements of air and ether (space). It represents energy, movement, and change. People with a predominant Vata dosha are creative, quick-thinking, and adaptable.")

# Pitta Dosha
with col2:
    st.image("https://i.imgur.com/UE2D26Z.png", caption="Pitta Dosha", width=image_width)
    st.write(
        "Pitta is linked to the elements of fire and water. It governs metabolism, digestion, and transformation. People with a predominant Pitta dosha tend to be determined, intelligent, and passionate.")

# Kapha Dosha
with col3:
    st.image("https://i.imgur.com/bx8owFD.png", caption="Kapha Dosha", width=image_width)
    st.write(
        "Kapha corresponds to the elements of earth and water. It provides stability and structure, leading to qualities of calmness, patience, and nurturing.")

# CTA (Call to Action)
st.header("Ready to Discover Your Dosha?")
st.image("https://i.imgur.com/wy3nGeh.jpg")
st.write("Get started with our Dosha assessment and prediction. Click the button below to begin!")

# Button to start assessment
if st.button("Take Assessment"):
    st.markdown('<a href="https://prakruti-kwvkhp7xc6tfba7ekepzpz.streamlit.app/#prakruti-vikruti-constitution-quiz" target="_blank">Start Assessment</a>', unsafe_allow_html=True)
    
st.write("OR") 
st.write("Scan the QR code to start the assessment")
st.image("https://i.imgur.com/SvVg5nD.png", width=100)

# Footer
st.write('The goal of life is to make your heartbeat match the beat of the universe, to match your nature with Nature. -Joseph Campbell”)
