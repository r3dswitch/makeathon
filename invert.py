from PIL import Image

def invert_image_colors(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Get pixel access object
    pixels = image.load()

    # Iterate over each pixel and invert its color
    for x in range(image.width):
        for y in range(image.height):
            # Get pixel value
            r, g, b = pixels[x, y]
            # Invert color
            inverted_r = 255 - r
            inverted_g = 255 - g
            inverted_b = 255 - b
            # Set inverted color to the pixel
            pixels[x, y] = (inverted_r, inverted_g, inverted_b)

    # Save the result image
    image.save(output_path)

# Example usage
image_path = "RPSO_palm_oil_bitmap.png"

invert_image_colors(image_path, image_path)