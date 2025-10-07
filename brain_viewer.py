import pyvista as pv

# Create a Plotter window
plotter = pv.Plotter(window_size=[900, 700])
plotter.background_color = "black"

# Add Attribution on top-right
attribution = '"Brain Realistic FREE" (https://skfb.ly/oOHxB) by darklord3d is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).'
plotter.add_text(attribution, position='upper_right', font_size=10, color='white', shadow=True)

# Load GLB brain model
# Replace 'brain_realistic_free.glb' with your actual path
try:
    brain = pv.read("brain_realistic_free.glb")
except Exception as e:
    print("Error loading brain model:", e)
    exit()

# Add brain to the scene
plotter.add_mesh(brain, color="lightgray", smooth_shading=True)

# Add lighting
plotter.add_light(pv.Light(position=(1, 1, 1), focal_point=(0,0,0), color='white', light_type='scene light'))
plotter.add_light(pv.Light(position=(-1, -1, 1), focal_point=(0,0,0), color='white', light_type='scene light'))

# Add axes
plotter.add_axes()

# Display
plotter.show(title="3D Brain Viewer")
