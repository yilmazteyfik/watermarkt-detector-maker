import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Simulated watermark detector
def detect_watermark(signal):
    watermark = np.array([0, 1, 0, 1])  # Sample watermark pattern
    correlation = np.correlate(signal.flatten(), watermark, mode='valid')
    return correlation.max()

# Simulated metal detection mechanism
def detect_metal(signal, metal_threshold):
    # Simulate metal detection by measuring the signal strength
    # If the signal strength exceeds the threshold, metal is detected
    signal_strength = np.abs(signal).mean()
    if signal_strength > metal_threshold:
        return True
    return False

def simulate_watermark_detection(signal, metal_threshold):
    if detect_metal(signal, metal_threshold):
        print("Metal detected! Oracle attack suspected.")
        return   
    
def watermark_detection(signal):
    watermark_strength = detect_watermark(signal)
    if watermark_strength > 0:
        print("Watermark detected.")
    else:
        print("No watermark detected.")

def process_image(image_path):
    # Load the image using PIL
    image = Image.open(image_path)
    # Convert the image to a numpy array
    signal = np.array(image)
    return signal

# Set the metal detection threshold
metal_threshold = 20

# Specify the path to the color image you want to process
image_path = 'example_image_watermaked2.jpg'
signal_with_watermark = process_image(image_path)

# Add simulated metal interference
metal_interference = np.random.normal(loc=0, scale=10, size=signal_with_watermark.shape)
signal_with_metal = signal_with_watermark + metal_interference

# Perform watermark detection with metal detection
simulate_watermark_detection(signal_with_metal, metal_threshold)
watermark_detection(signal_with_metal)

# Display the original and metal-affected images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(signal_with_watermark)
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(signal_with_metal)
plt.title("Metal-Affected Image")
plt.show()
