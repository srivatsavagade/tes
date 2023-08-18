import streamlit as st
from PIL import Image
import pytesseract
import os
import pandas as pd

st.title('OCR and Data Extraction App')

# Path to the Tesseract executable
tesseract_path = '/app/.apt/usr/bin/tesseract'  # This path works on Streamlit Sharing

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    extracted_text = pytesseract.image_to_string(image, config=f'--tessdata-dir {os.path.dirname(tesseract_path)}')

    st.subheader('Extracted Text:')
    st.write(extracted_text)

    # Process extracted text and display as a DataFrame
    rows = extracted_text.split('\n')
    data = [row.split() for row in rows if row.strip()]
    df = pd.DataFrame(data)
    st.subheader('Extracted Data:')
    st.write(df)
