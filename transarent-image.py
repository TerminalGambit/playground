from PIL import Image

# Define the dimensions of the image
width, height = 64, 64

# Create a transparent image
transparent_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Save the image
file_name = "empty_texture.png"
transparent_image.save(file_name, "PNG")

print(f"Transparent texture created and saved as {file_name}")