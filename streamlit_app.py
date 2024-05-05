import streamlit as st
import requests
from PIL import Image
import io

st.title('EcoTrack Recycling Assistant')

st.write("Welcome to EcoTrack, your smart AI-powered recycling assistant!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Prepare the image to send to Flask
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()
    
    # Send the image to Flask, ensuring the name matches and including the MIME type
    response = requests.post(
        'http://127.0.0.1:5000/predict',
        files={"file": ("filename.jpg", image_bytes, "image/jpeg")}
    )
    
    if response.status_code == 200:
        # Display the prediction result
        result = response.json()
        st.write(f"Predicted class: {result['predicted_class']}")
    else:
        st.error(f"Failed to get prediction from the server. Status code: {response.status_code}")
