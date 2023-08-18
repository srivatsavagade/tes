import streamlit as st
from rembg import remove
from PIL import Image
import pytesseract
import io

def main():
    st.title("Background Removal and OCR App")

    image_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Original Image', use_column_width=True)

        if st.button("Remove Background and Extract Text"):
            with st.spinner("Processing..."):
                # Remove background
                result_image = remove(image)

                # Perform OCR on the background-removed image
                pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'
                extracted_text = pytesseract.image_to_string(result_image)
                st.text("Extracted Text:")
                st.text(extracted_text)

                # Display the background-removed image with extracted text
                st.image(result_image, caption='Background Removed', use_column_width=True)

                # Convert the PIL Image to bytes
                result_image_bytes = io.BytesIO()
                result_image.save(result_image_bytes, format='PNG')
                result_image_bytes = result_image_bytes.getvalue()

                # Create a download button for the background-removed image
                st.download_button(
                    label="Download Processed Image",
                    data=result_image_bytes,
                    file_name="background_removed.png"
                )

if __name__ == "__main__":
    main()
