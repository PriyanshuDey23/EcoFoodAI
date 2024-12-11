import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
from EcoFoodAI.helper import *
from EcoFoodAI.prompt import *  # Import the prompt from an external module
from EcoFoodAI.utils import *

# Initialize the Streamlit app
st.set_page_config(page_title="Eco Food Analysis", page_icon="🍎", layout="centered")
st.title("🍎 Eco Food Carbon Footprint Analysis")

# Load Lottie animation
animation_url = "https://assets9.lottiefiles.com/packages/lf20_q5pk6p1k.json"
carbon_animation = load_lottie_url(animation_url)
if carbon_animation:
    st_lottie(carbon_animation, height=200, key="carbon")

# Brief introduction to guide the user
st.markdown("""
Welcome to **Eco Food**! 🌟 Upload a food image and get an estimated carbon footprint of the meal.
This tool will analyze the food items, categorize them, estimate their weights, and calculate the total carbon emissions associated with your meal.
""")

# File uploader for images (supports jpg, jpeg, and png)
uploaded_file = st.file_uploader("**Upload your food image 📂**", type=["jpg", "jpeg", "png","jfif"])

# Display the uploaded image
if uploaded_file is not None:
    st.success("**📥 File Uploaded Successfully! 🎉**")
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Meal Image", use_column_width=True)

# Button to trigger the carbon footprint analysis
if st.button("**✨ Analyze Carbon Footprint ✨**"):
    if uploaded_file is not None:
        try:
            # Prepare the image data for the model
            image_data = prepare_image(uploaded_file)
            response = get_gemini_response(image_content=image_data, prompt=PROMPT)

            # Display the response from the model (Carbon Footprint analysis)
            st.subheader("**🍽️ Estimated Carbon Footprint**")
            st.write(response)

            # Interactive tips to reduce carbon footprint
            st.markdown("""
            **What can you do to reduce your carbon footprint? 🌎**
            """)
            st.checkbox("Reduce meat consumption")
            st.checkbox("Use public transport or walk/bike")
            st.checkbox("Use energy-efficient appliances")
            st.checkbox("Recycle and compost")

            # Carbon Footprint Breakdown Visualization
            st.subheader("**Carbon Footprint Breakdown**")
            labels = ["Food Production", "Transportation", "Cooking"]
            values = [40, 30, 30]

            # Create a pie chart using Plotly
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
            fig.update_layout(title_text="Carbon Footprint Components")
            st.plotly_chart(fig)

            # Create a Word document with the analysis
            docx_file = create_docx(response)

            # Display the download button for the Word document
            st.download_button(
                label="Download Full Report",
                data=docx_file,
                file_name="EcoFood_Carbon_Footprint_Report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image to proceed!")

# Additional information or tips for users
st.markdown("""
**Note:**
- The analysis is based on image content and may involve some estimation.
- The carbon footprint values are calculated based on average data for typical food items.
""")

# Display a loading animation while the analysis is being performed
with st.spinner("Analyzing carbon footprint..."):
    pass
