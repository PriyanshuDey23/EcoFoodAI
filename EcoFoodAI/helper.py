from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests


# Load environment variables from .env file
load_dotenv()

# Set up the API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the Gemini model
def get_gemini_response(image_content, prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Using the Flash version of the Gemini model
    response = model.generate_content([image_content[0], prompt])
    return response.text

# Function to convert the uploaded image to bytes
def prepare_image(uploaded_file):
    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": image_bytes}]
    else:
        raise FileNotFoundError("No file uploaded")

# Function to load Lottie animations
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
