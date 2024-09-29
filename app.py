import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Video Background", layout="centered")

# Custom CSS for video background
st.markdown(
    """
    <style>
    .video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
    }
    .centered-button {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Embed the video in the background
components.html(
    """
    <video autoplay loop muted class="video-background">
        <source src="tech_music.mp4" type="video/mp4">
    </video>
    """,
    height=0,  # height set to 0 to hide the component space in the layout
)

# Display the centered button
st.markdown(
    """
    <div class="centered-button">
        <button>Play</button>
    </div>
    """,
    unsafe_allow_html=True
)
