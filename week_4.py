from PIL import Image
from pydub.generators import Sine
import os
import random


def pixel_to_sound(image_path, output_dir, num_sounds=10, duration_ms=200):
 
    img = Image.open(image_path)
    img = img.convert("L")  
    width, height = img.size


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    selected_pixels = [
        (random.randint(0, width - 1), random.randint(0, height - 1))
        for _ in range(num_sounds)
    ]

    for i, (x, y) in enumerate(selected_pixels):

        brightness = img.getpixel((x, y))
        
      
        freq = 100 + (brightness / 255) * 900 
        

        volume = -30 + (brightness / 255) * 30
     
        tone = Sine(freq).to_audio_segment(duration=duration_ms, volume=volume)
        
        filename = f"{output_dir}/tone_{i + 1}.wav"
        tone.export(filename, format="wav")

    print(f"Generated {num_sounds} sound files in '{output_dir}'.")


image_path = "example_image.jpg"  
output_dir = "output_sounds"
pixel_to_sound(image_path, output_dir, num_sounds=10)
