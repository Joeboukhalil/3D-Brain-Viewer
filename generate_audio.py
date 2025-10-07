# generate_audio.py
from gtts import gTTS
import os

texts = {
    "frontal_lobe.mp3": "The frontal lobe controls reasoning, movement, emotions, and problem solving.",
    "parietal_lobe.mp3": "The parietal lobe processes touch, pressure, temperature, and spatial orientation.",
    "temporal_lobe.mp3": "The temporal lobe handles hearing, memory, and language understanding.",
    "occipital_lobe.mp3": "The occipital lobe is responsible for visual processing.",
    "cerebellum.mp3": "The cerebellum coordinates balance and precise movement.",
    "brainstem.mp3": "The brainstem controls breathing, heart rate, and vital body functions."
}

os.makedirs("sounds", exist_ok=True)

for filename, text in texts.items():
    tts = gTTS(text)
    path = os.path.join("sounds", filename)
    tts.save(path)
    print("Created:", path)

print("✅ All audio files generated in /sounds/")
