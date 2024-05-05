import streamlit as st
import requests
from PIL import Image
import io

st.title('EcoTrack Recycling Assistant')

st.write("Welcome to EcoTrack, your smart AI-powered recycling assistant!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    # Assuming the image is in PIL format
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Image is uploaded. Processing will be here...")
    
    # Prepare the image to send to Flask
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()
    
    # Send the image to Flask
    response = requests.post(
        'http://localhost:5000/predict', 
        files={"image": image_bytes}
    )
    
    if response.status_code == 200:
        # Display the prediction result
        result = response.json()
        st.write(f"Predicted class: {result['class']}")
    else:
        st.error("Failed to get prediction from the server.")

