import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

# Page Configuration
st.set_page_config(
    layout="wide", 
    page_title="Professional Image Background Remover",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown(
    """
    <style>
    /* Global Style */
    body {
        background-color: #f4f4f9;  /* Light gray background color */
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
    }

    /* Title Styling */
    h1 {
        color: #004085;  /* Dark blue color */
        font-size: 2.5em;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Upload text color change */
    .upload-text {
        color: #495057;  /* Dark gray color */
        font-size: 1.2em;
        text-align: center;
    }

    /* Image hover effect */
    .stImage img:hover {
        transform: scale(1.05);
        transition: transform 0.3s ease;
        cursor: pointer;
    }

    /* Button hover effect */
    .stButton button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        padding: 12px 25px;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #0056b3;
    }

    /* Image Container */
    .stImage img {
        border-radius: 10px;
        border: 2px solid #ddd;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f0f4f7;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Sidebar styling */
    .sidebar {
        width: 280px;
        padding-top: 20px;
    }

    /* Spinner Styling */
    .stProgress > div {
        background-color: #007bff;
    }

    /* Columns styling */
    .col-image {
        width: 45%;
        padding: 10px;
    }
    .main-title {
            font-size: 48px;
            font-weight: bold;
            color: #16a085;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 40px;
        }
        
    .sidebar-button {
            font-size: 16px;
            padding: 12px 20px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            text-decoration: none;
            color: white;
            background-color: #34495e; /* Dark Button Background */
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }

        .sidebar-button:hover {
            background-color: #1abc9c; /* Teal Hover Effect */
            color: white;
            transform: scale(1.05); /* Slightly enlarge on hover */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# # Page Title and Description
# st.write(
#     "<h1></h1>",
#     unsafe_allow_html=True
# )
# Title for the homepage
st.markdown('<h1 class="main-title" style="border:1px solid #16a085">✨ Image Background Remover ✨</h1>', unsafe_allow_html=True)


st.write(
    '<p class="sidebar-button">Upload your image to remove its background. It\'s easy and quick. Just fill out the form and we\'ll process your image in no time!</p>',
    unsafe_allow_html=True
)

# Form Layout for Image Upload
with st.form(key='image_upload_form'):
    st.write("## Upload Image")
    my_upload = st.file_uploader("Choose an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    submit_button = st.form_submit_button(label="Process Image")

    # File Size Limit
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


# Function to Convert Image for Download
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Handle Image Processing
if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    elif submit_button:
        # Show Spinner while Processing
        with st.spinner("Processing your image..."):
            # Open and process the image
            image = Image.open(my_upload)
            fixed_image = remove(image)

            # Create two columns for side-by-side display
            col1, col2 = st.columns(2)

            # Display the uploaded image on the left (col1)
            col1.write("### Original Image :camera:")
            col1.image(image, use_column_width=True)

            # Display the processed image on the right (col2)
            col2.write("### Fixed Image :wrench:")
            col2.image(fixed_image, use_column_width=True)

            # Provide Download Button for Fixed Image
            st.markdown("\n")
            st.download_button("Download Fixed Image", convert_image(fixed_image), "fixed.png", "image/png")
            
else:
    st.warning("Please upload an image to get started.")
