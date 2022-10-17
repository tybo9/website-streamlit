import json
from threading import local
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style/style.css")

# --- Load Assets ---
##lottie_coding = load_lottiefile("potato.json")
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_es4p9zph.json")
#img_contact_form = Image.open("images/imag1.png")
#img_contact_form = Image.open("images/imag2.png")
img_lottie_animation = Image.open("images/imag3.png")

# ---- Header Section ----
with st.container():
     st.subheader("Hello, I am Ayoub :wave:")
     st.title("A Computer Sciencitst")
     st.write("""I am a recent graduate earning a Bachelor's degree in Computer Science from San Diego State University. I am self-motivated, hardworking, and passionate about learning new technlogies. 
                 I am also interested in working on projects that involve web development and mobile development. 
                 The best way to reach me is through contact form below. I look forward to hearing from you!""")
# ---- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write (
            """I like working on projects that involve data science, machine learning, web development, and mobile development. Complex problems that require creative solutions are my favorite.
                 Besides that, I also like to play soccer, travel, hangout with friends, workout and snowboarding. I am also a big fan of soccer team like Real Madrid."""  
                 )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.image(img_lottie_animation)
with text_column:
    st.subheader("coming soon")
    st.write("""I am working on the self project to build a web app. This is just running on local device, and soon will be publish to public""")
# ---- Contact Form ---
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
 # Documentation: https://formsubmit.co/ !!!
    contact_form = """
 <form action="https://formsubmit.co/rammo.ayoub7@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Contact Form")
        st.write(contact_form, unsafe_allow_html=True)
    with right_column:
        ##st.markdown(contact_form, unsafe_allow_html=True)
    ##with right_column:
       st.empty()
       
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 