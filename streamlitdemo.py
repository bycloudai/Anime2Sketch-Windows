import streamlit as st
import os
from data import get_image_list
from model import create_model
from data import read_img_path, tensor_to_img, IMG_EXTENSIONS
from PIL import Image
import torch
import gdown
import urllib.request

@st.cache()
def download_model():
    url = "https://drive.google.com/uc?id=1RILKwUdjjBBngB17JHwhZNBEaW4Mr-Ml"
    output = "weights/netG.pth"
    with st.spinner("Model weights were not found, downloading. Please wait🙏"):
        download_model = gdown.download(url, output, quiet=False)   
    # return download_model

# @st.cache
# def download_model():
#     MODEL_PATH = './weights/netG.pth'

#     if not os.path.exists(MODEL_PATH):
#         decoder_url = 'wget -O ./weights/netG.pth https://drive.google.com/uc?id=1RILKwUdjjBBngB17JHwhZNBEaW4Mr-Ml'

#         with st.spinner("Done! \n Model weights were not found, downloading..."):
#             os.system(decoder_url)
#     else:
#         print("Model found")

@st.cache()
def load_model():
    gpu_ids=[]
    model = create_model(gpu_ids)
    model.eval()
    return model

st.title("Anime2Sketch")

st.text("Demo for Anime2Sketch Streamlit version. To use it, simply upload your images or click one of the examples to load them.")
def main():

    selected_box = st.sidebar.selectbox(
        "Choose one of the following", 
        ("Image from Examples", "Upload Image")
    )

    if selected_box == "Image from Examples":
        examples()
    
    if selected_box == "Upload Image":
        upload()

def examples():
    img = st.sidebar.selectbox(
        'Select Image', 
        ('Wave', 'Building', 'Madoka')
    )
    
    st.header('Original')
    if img == 'Wave':
        image = Image.open('wave.jpg')
        show = st.image(image, use_column_width = True)

    if img == 'Building':
        image = Image.open('building.jpg')
        show = st.image(image, use_column_width = True)

    if img == 'Madoka':
        image = Image.open('test_samples/madoka.jpg')
        show = st.image(image, use_column_width = True)

    st.header('Anime2Sketch')
    new_img = anime2sketch(img)
    st.image(new_img, use_column_width = True)

def upload():
    st.write("Source Image")
    uploaded_file = st.file_uploader("Choose an image", type=IMG_EXTENSIONS)

    if uploaded_file is not None:
        st.header('Original')
        image = Image.open(uploaded_file)
        show = st.image(image, use_column_width = True)
        
    clicked = st.button("Process")
    
    if clicked:
        model = anime2sketch(image)
        st.header('Anime2Sketch')
        st.image(model, use_column_width = True)


a = 'wave.jpg'
b = 'building.jpg'
c = 'test_samples/madoka.jpg'

def anime2sketch(img_input, load_size=512):
    img, aus_resize = read_img_path(c, load_size)
    model = load_model()
    aus_tensor = model(img)
    aus_img = tensor_to_img(aus_tensor)
    image_pil = Image.fromarray(aus_img)
    image_pil = image_pil.resize(aus_resize, Image.BICUBIC)
    return image_pil

if __name__ == '__main__':
    download_model()
    main()