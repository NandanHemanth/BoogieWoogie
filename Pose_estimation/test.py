import cv2
import mediapipe as mp
import numpy as np
import pygame
from pygame import mixer
from PIL import Image
import time
from pygltflib import GLTF2
import pythreejs as p3


# Initialize MediaPipe pose detection
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

fps = 0

# Initialize pygame for music
pygame.init()
mixer.init()

# Load music (replace 'your_song.mp3' with the path to your music file)
mixer.music.load('JD_americano.mp3')
mixer.music.play(-1)  # Loop the music indefinitely

# Load and parse the 3D GLB disco ball
gltf = GLTF2().load('disco_ball.glb')

# Setup 3D rendering with pythreejs (for example, you need to setup 3D rendering separately)
# Render the disco ball using pythreejs (example code can be complex)

# Video capture
cap = cv2.VideoCapture(0)

# # Function to render the 3D disco ball (this part requires a rendering setup)
# def render_disco_ball():
#     # Implement the 3D model rendering and return as an image frame
#     # Example: Using pythreejs or PyOpenGL for rendering
#     pass

def render_disco_ball():
    """
    Function to render the 3D disco ball model (.glb) and return it as an image frame.
    This implementation uses pythreejs for rendering.
    """
    # Load the GLB file
    gltf = GLTF2().load('disco_ball.glb')
    
    # Set up a scene with pythreejs
    scene = p3.Scene()

    # Set up a perspective camera
    camera = p3.PerspectiveCamera(position=[0, 0, 2], aspect=1, fov=75, near=0.1, far=1000)

    # Set up the renderer
    renderer = p3.Renderer(
        camera=camera,
        scene=scene,
        alpha=True,  # To support transparency
        antialias=True,
        width=512,
        height=512
    )

    # Set up the ambient lighting
    ambient_light = p3.AmbientLight(color='white', intensity=1)
    scene.add(ambient_light)

    # Set up point light for a disco effect
    point_light = p3.PointLight(color='white', position=[1, 1, 1], intensity=1.5)
    scene.add(point_light)

    # Load the GLTF model into the scene
    loader = p3.GLTFLoader()
    model = loader.parse(gltf.model)
    scene.add(model)

    # Render the scene to a texture
    renderer.render(scene, camera)

    # Convert the rendered texture to an image (PIL format)
    frame = renderer.dom_element  # This grabs the canvas from the renderer
    pil_image = Image.frombytes('RGBA', frame.size, frame.data)
    
    # Convert the PIL image to a numpy array for OpenCV compatibility
    image_np = np.array(pil_image)

    # Resize or process the image as needed (e.g., scale to fit video dimensions)
    return image_np

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    fps_start_time = time.time()
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break
        
        # Recolor image to RGB for MediaPipe processing
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make pose detection
        results = pose.process(image)

        # Recolor back to BGR for OpenCV display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Render the pose landmarks
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))
        
        # Render the 3D disco ball (you will need to implement this part)
        disco_ball_frame = render_disco_ball()  # Render the 3D model into an image frame

        if disco_ball_frame is not None:
            # Overlay the 3D rendered disco ball onto the video feed
            # Assuming disco_ball_frame is an image, blend it on top of `image`
            image = cv2.addWeighted(image, 0.8, disco_ball_frame, 0.2, 0)

        # Calculate and display FPS
        frame_count += 1
        elapsed_time = time.time() - fps_start_time
        
        if elapsed_time > 1:  # Update FPS every second
            fps = frame_count / elapsed_time
            fps_start_time = time.time()
            frame_count = 0

        # Put FPS text on the image
        cv2.putText(image, f'FPS: {int(fps)}', (image.shape[1] - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the image with the augmented elements
        cv2.imshow('Mediapipe + Disco Ball', image)

        # Exit on pressing 'Esc'
        if cv2.waitKey(10) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    mixer.music.stop()  # Stop the music
