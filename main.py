# main.py
import pyvista as pv
import pygame
import threading

pygame.mixer.init()

def play_audio(file):
    def _play():
        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        except Exception as e:
            print("Audio error:", e)
    threading.Thread(target=_play, daemon=True).start()

plotter = pv.Plotter(window_size=[1000, 800])
plotter.background_color = "black"

# Attribution
plotter.add_text(
    '"Brain Realistic FREE" (https://skfb.ly/oOHxB)\n'
    'by darklord3d — CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/)',
    position='upper_right', font_size=10, color='white'
)

# Load your real model
brain = pv.read("brain_realistic_free.glb")
plotter.add_mesh(brain, color="lightgray", smooth_shading=True)

# Detect click regions (approximation)
def click_callback(point):
    if point is None:
        return
    x, y, z = point
    print(f"Clicked at {x:.2f}, {y:.2f}, {z:.2f}")
    # Adjust coordinate thresholds depending on your model scale
    if x > 0.02 and z > 0:
        print("→ Frontal Lobe")
        play_audio("sounds/frontal_lobe.mp3")
    elif x < -0.02 and z > 0:
        print("→ Parietal Lobe")
        play_audio("sounds/parietal_lobe.mp3")
    elif z < -0.05:
        print("→ Cerebellum")
        play_audio("sounds/cerebellum.mp3")
    elif y < -0.05:
        print("→ Brainstem")
        play_audio("sounds/brainstem.mp3")
    elif y > 0.03 and z > 0:
        print("→ Temporal Lobe")
        play_audio("sounds/temporal_lobe.mp3")
    else:
        print("→ Occipital Lobe")
        play_audio("sounds/occipital_lobe.mp3")

plotter.enable_point_picking(callback=click_callback, show_message=True)
plotter.add_axes()
plotter.show(title="Interactive Talking Brain")
