# import streamlit as st
# import base64
# import os
# import time

# # Path to your GIF file
# file_path = "C:/Users/ndkrd/OneDrive/Desktop/giphy.gif"  # Local file for testing
# gif_data = ""

# # Check if the GIF file exists and encode it in base64
# if os.path.exists(file_path):
#     with open(file_path, "rb") as file_:
#         contents = file_.read()
#         gif_data = base64.b64encode(contents).decode("utf-8")
# else:
#     st.write("Error: GIF file not found.")

# # Custom CSS for fade-in, fade-out, sparkling effect with silver color, Algerian font, and black outline
# st.markdown(f"""
#     <style>
#     @import url('https://fonts.cdnfonts.com/css/algerian'); /* Import Algerian font */

#     html, body {{
#         overflow: hidden;  /* Disable vertical and horizontal scrolling */
#     }}
#     .main {{
#         background-image: url("data:image/gif;base64,{gif_data}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#         height: 100vh;  /* 100% of the viewport height */
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         flex-direction: column;
#         padding: 0;
#         margin: 0;
#     }}
    
#     /* Keyframes for sparkling effect */
#     @keyframes sparkle {{
#         0%, 100% {{
#             text-shadow: 
#                 2px 2px 0px #000000, /* Black outline */
#                 -2px -2px 0px #000000, 
#                 2px -2px 0px #000000, 
#                 -2px 2px 0px #000000,
#                 0px 0px 15px #ffffff; /* White inner glow for sparkle */
#         }}
#         50% {{
#             text-shadow: 
#                 2px 2px 0px #000000, /* Black outline */
#                 -2px -2px 0px #000000, 
#                 2px -2px 0px #000000, 
#                 -2px 2px 0px #000000,
#                 0px 0px 20px #C0C0C0; /* Sparkling silver shadow */
#         }}
#     }}
    
#     /* Keyframes for fadeIn and fadeOut */
#     @keyframes fadeIn {{
#         0% {{ opacity: 0; }}
#         100% {{ opacity: 1; }}
#     }}
#     @keyframes fadeOut {{
#         0% {{ opacity: 1; }}
#         100% {{ opacity: 0; }}
#     }}
    
#     .title {{
#         font-family: 'Algerian', arial;
#         font-size: 3.5rem;
#         color: silver;  /* Set font color to silver */
#         text-shadow: 
#             2px 2px 0px #000000, /* Black outline */
#             -2px -2px 0px #000000, 
#             2px -2px 0px #000000, 
#             -2px 2px 0px #000000, 
#             0px 0px 8px #ffffff;  /* White glow */
#         animation: fadeIn 2s ease-in-out forwards, fadeOut 3s ease-in-out 5s forwards, sparkle 2s infinite;
#         transition: opacity 1s ease-in-out;
#         /* Sparkle effect runs infinitely and title fades in/out */
#     }}
    
#     /* Center the button */
#     .play-container {{
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-50%, -50%);
#         text-align: center;
#         width: 100px;
#     }}

#     .play-button {{
#         font-family: 'Algerian', arial;
#         font-size: 2rem;
#         color: silver;
#         cursor: pointer;
#         text-shadow: 
#             2px 2px 0px #000000, /* Black outline */
#             -2px -2px 0px #000000, 
#             2px -2px 0px #000000, 
#             -2px 2px 0px #000000, 
#             0px 0px 8px #ffffff;  /* White glow */
#         transition: opacity 1s ease-in-out;
#         border: 2px solid silver;
#         padding: 10px 20px;
#         background-color: rgba(0, 0, 0, 0.5); /* Transparent background */
#     }}
    
#     </style>
# """, unsafe_allow_html=True)

# # Display the animated, sparkling game title with silver color, Algerian font, and black outline
# st.markdown('<div class="main"><h1 class="title"> Boogie Box </h1></div>', unsafe_allow_html=True)

# # Time to wait before showing the PLAY button (this matches the fade-out time of the title)
# time.sleep(7)  # Adjust the time to match the fade-out animation (2s fadeIn + 5s display + 3s fadeOut)

# # Use a form to handle the submission for the button click
# with st.form("my_form"):
#     st.markdown('''
#     <div class="play-container">
#         <button class="play-button" type="submit">PLAY</button>
#     </div>
#     ''', unsafe_allow_html=True)

#     # This is where the form submit button is checked
#     submit_button = st.form_submit_button("PLAY")

# if submit_button:
#     with st.spinner('Loading...'):
#         # Simulate a progress bar
#         progress_bar = st.progress(0)
#         for percent_complete in range(100):
#             time.sleep(0.05)  # Adjust this sleep time to make loading faster/slower
#             progress_bar.progress(percent_complete + 1)

import streamlit as st
import base64
import os
import time

# Path to your GIF file
file_path = "C:/Users/ndkrd/OneDrive/Desktop/giphy.gif"  # Local file for testing
gif_data = ""

# Check if the GIF file exists and encode it in base64
if os.path.exists(file_path):
    with open(file_path, "rb") as file_:
        contents = file_.read()
        gif_data = base64.b64encode(contents).decode("utf-8")
else:
    st.write("Error: GIF file not found.")

# Custom CSS for the background, central button, and larger Play button with Algerian font
st.markdown(f"""
    <style>
    @import url('https://fonts.cdnfonts.com/css/algerian'); /* Import Algerian font */

    html, body {{
        overflow: hidden;  /* Disable vertical and horizontal scrolling */
    }}
    .main {{
        background-image: url("data:image/gif;base64,{gif_data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;  /* 100% of the viewport height */
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        padding: 0;
        margin: 0;
    }}
    
    /* Keyframes for fadeIn and fadeOut */
    @keyframes fadeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}
    @keyframes fadeOut {{
        0% {{ opacity: 1; }}
        100% {{ opacity: 0; }}
    }}
    
    .title {{
        font-family: 'Algerian', arial;
        font-size: 3.5rem;
        color: silver;  /* Set font color to silver */
        text-shadow: 
            2px 2px 0px #000000, /* Black outline */
            -2px -2px 0px #000000, 
            2px -2px 0px #000000, 
            -2px 2px 0px #000000, 
            0px 0px 8px #ffffff;  /* White glow */
        animation: fadeIn 2s ease-in-out forwards, fadeOut 3s ease-in-out 5s forwards;
    }}

    /* Style for the container with the title and play button */
    .center {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
        flex-direction: column;
    }}
    
    /* Style for the Play button with doubled size, Algerian font, moved up and right */
    div.stButton > button {{
        font-family: 'Algerian', arial !important;
        font-size: 30rem !important;  /* Double font size */
        padding: 40px 80px !important;  /* Double the padding for button size */
        color: silver !important;
        background-color: rgba(0, 0, 0, 0.7) !important;
        border: 4px solid silver !important;  /* Double the border width */
        border-radius: 20px !important;
        text-shadow: 
            2px 2px 0px #000000, /* Black outline */
            -2px -2px 0px #000000, 
            2px -2px 0px #000000, 
            -2px 2px 0px #000000, 
            0px 0px 8px #ffffff !important;  /* White glow */
        cursor: pointer;
        transform: translate(200px, -200px) !important;  /* Move 200px right and 200px up */
    }}
    
    /* Change hover color to grey */
    div.stButton > button:hover {{
        background-color: grey !important;  /* Set hover color to grey */
    }}
    </style>
""", unsafe_allow_html=True)

# Display the animated, sparkling game title with silver color, Algerian font, and black outline
st.markdown('<div class="main"><h1 class="title"> Boogie Box </h1></div>', unsafe_allow_html=True)

# Placeholder to manage when the button appears
placeholder = st.empty()

# Use the placeholder for the button after title fades out
time.sleep(7)  # Wait for the title to disappear (2s fadeIn + 5s display + 3s fadeOut)

# Display only the Streamlit button moved up and right
with placeholder.container():
    play_button = st.button("**PLAY**")  # This button is centrally aligned but moved up and right

# If the play button is clicked, show the progress bar
if play_button:
    with st.spinner('Loading...'):
        # Simulate a progress bar
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.05)  # Adjust this sleep time to control the loading speed
            progress_bar.progress(percent_complete + 1)
        
    st.success('Game Ready!')


# import spotipy 
# from spotipy.oauth2 import SpotifyOAuth

# # Set up your credentials from the Spotify Developer Dashboard
# client_id = 'a0a7a69f20364f6f83e7613089149645'
# client_secret = '2b7837c23b504c00b24dc483aa16c7c2'
# redirect_uri = 'https://discodaddy.us'  # You can use any localhost URI for testing

# # Scope required to access liked songs (user-library-read)
# scope = 'user-library-read'

# # Set up authentication
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
#                                                client_secret=client_secret,
#                                                redirect_uri=redirect_uri,
#                                                scope=scope))

# # Function to get liked songs
# def get_liked_songs():
#     results = sp.current_user_saved_tracks()
#     liked_songs = []

#     while results:
#         for idx, item in enumerate(results['items']):
#             track = item['track']
#             liked_songs.append({
#                 'name': track['name'],
#                 'artist': ', '.join([artist['name'] for artist in track['artists']]),
#                 'album': track['album']['name'],
#                 'release_date': track['album']['release_date']
#             })

#         # If there are more tracks, get the next page
#         if results['next']:
#             results = sp.next(results)
#         else:
#             results = None

#     return liked_songs

# # Fetch liked songs
# liked_songs = get_liked_songs()

# # Print the liked songs
# for idx, song in enumerate(liked_songs):
#     print(f"{idx + 1}. {song['name']} by {song['artist']} from the album '{song['album']}' (Released on {song['release_date']})")