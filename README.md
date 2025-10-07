# Interactive 3D Brain Viewer

An interactive 3D brain viewer built in Python using PyVista, allowing users to explore the human brain and hear explanations about its different regions.

---

## Project Overview

This project has two main components:

1. **Brain Viewer (`main.py`)**  
   - Displays a 3D brain model using PyVista.
   - Users can click on specific brain regions (marked with red points).
   - Each click plays a voice explanation of the selected region using `pyttsx3`.
   
2. **Sound Generator (Optional)**  
   - Audio explanations for each brain region can be pre-generated using Google Text-to-Speech (`gTTS`).
   - Generated `.mp3` files are stored in the `sounds/` folder and can be used in `main.py`.

---

## Project Structure

BrainViewer/
│
├── main.py # Main script to launch the interactive 3D brain viewer
├── brain_points.py # Coordinates and names of brain regions
├── brain_realistic_free.glb # 3D brain model
└── sounds/ # Audio explanations for each brain region
├── frontal_lobe.mp3
├── parietal_lobe.mp3
├── temporal_lobe.mp3
├── occipital_lobe.mp3
├── cerebellum.mp3
└── brainstem.mp3


---

## Installation

Install the required Python packages (tested with Python 3.13):

```bash py -3.13 -m pip install pyvista pyttsx3 gtts```


## Usage

Make sure the 3D model (brain_realistic_free.glb) is in the project folder.

Run the main viewer:

```bash py -3.13 main.py```


Click on any red point in the 3D model:

The program will display the brain region name.

The computer will speak a brief explanation of the selected brain region.



## 3D Model Attribution

The brain model used in this project is:

"Brain Realistic FREE"
by darklord3d

Licensed under Creative Commons Attribution (CC BY 4.0)

You are free to use, share, and adapt the model as long as proper credit is given.


## Notes

The brain viewer is designed for interactive learning and visualization.

Coordinates for brain regions in brain_points.py may need fine-tuning depending on the model scale.


## License

This project itself is shared under MIT LICENSE license, but the 3D model requires attribution as noted above.
