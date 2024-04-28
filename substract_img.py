from PIL import Image

def subtract_images(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Ensure the images have the same size
    if image1.size != image2.size:
        raise ValueError("Images must have the same dimensions")

    # Get pixel access objects
    pixels1 = image1.load()
    pixels2 = image2.load()
    
    # Create a new image for the result
    result_image = Image.new("RGB", image1.size)

    # Iterate over each pixel and subtract corresponding pixel values
    for x in range(image1.width):
        for y in range(image1.height):
            # Get pixel values from each image
            r1, g1, b1, a1 = pixels1[x, y]
            r2, g2, b2, a2 = pixels2[x, y]
            # Perform subtraction and ensure the result is within 0-255 range
            r = max(0, min(r1 - r2, 255))
            g = max(0, min(g1 - g2, 255))
            b = max(0, min(b1 - b2, 255))
            # Set the pixel value in the result image
            result_image.putpixel((x, y), (r, g, b))

    # Save the result image
    result_image.save(output_path)

# Example usage
image2_path = "RPSO_palm_oil.png"
image1_path = "no_label.png"
output_path = "RPSO_palm_oil_bitmap.png"

subtract_images(image1_path, image2_path, output_path)
