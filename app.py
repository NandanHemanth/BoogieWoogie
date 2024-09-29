import streamlit as st

# Video background using HTML and CSS
st.markdown(
    """
    <style>
    .video-container {
        position: fixed;
        top: 0;
        left: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
    }

    .content {
        position: relative;
        z-index: 2;
        text-align: center;
    }

    .button {
        position: fixed;
        bottom: 50px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 3;
    }

    .leaderboard {
        display: none;
        position: fixed;
        bottom: 100px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 3;
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    <div class="video-container">
        <video autoplay loop muted>
            <source src="your_video_url.mp4" type="./neon_disco.mp4">
        </video>
    </div>
    """,
    unsafe_allow_html=True
)

# Content to overlay on top of the video
st.markdown('<div class="content">', unsafe_allow_html=True)

# Center button
if st.button('Click Me!', key="center_button"):
    st.write("Button clicked!")

# Leaderboard toggle
show_leaderboard = st.checkbox('Show Leaderboard', key="toggle_leaderboard")

if show_leaderboard:
    st.markdown('<div class="leaderboard">', unsafe_allow_html=True)
    st.write("Leaderboard")
    st.write("1. User1 - 100 Points")
    st.write("2. User2 - 90 Points")
    st.write("3. User3 - 80 Points")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
