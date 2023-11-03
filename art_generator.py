from PIL import Image, ImageDraw

def generate_art():

    image = Image.new(
        mode="RGB",
        size=(128, 128),
        color='black'
    )

    draw = ImageDraw.Draw(image)
    line_xy = ((0, 0), (128, 128))
    draw.line(line_xy, fill="white")

    image.save("test_image.png")

if __name__ == "__main__":
    generate_art()