from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the input image
    image = Image.open(input_image_path)

    # Create a white background image with the same size as the input image
    background = Image.new('RGB', image.size, (255, 255, 255))

    # Create a transparent layer with the same size as the image
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

    # Choose a font (adjust the path and size as needed)
    font = ImageFont.truetype('arial.ttf', 36)

    # Create a drawing object
    draw = ImageDraw.Draw(watermark)

    # Calculate the position for the watermark (adjust the x and y values as needed)
    text_width, text_height = draw.textsize(watermark_text, font)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2

    # Draw the watermark text on the transparent layer
    draw.text((x, y), watermark_text, font=font)

    # Combine the background image, input image, and watermark layer
    watermarked = Image.alpha_composite(background.convert('RGBA'), image.convert('RGBA'))
    watermarked = Image.alpha_composite(watermarked, watermark)

    # Convert the image to RGB mode before saving as JPEG
    watermarked = watermarked.convert('RGB')

    # Save the watermarked image
    watermarked.save(output_image_path)


# Example usage
add_watermark('C:\\Users\\sarper.sarp\\Desktop\\phyton\\example_image2.jpg', 'C:\\Users\\sarper.sarp\\Desktop\\phyton\\example_image_watermarked2.jpg', 'Watermark Text')
