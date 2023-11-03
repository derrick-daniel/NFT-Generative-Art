from PIL import Image, ImageDraw
import random

def generate_art():

    image = Image.new(
        mode="RGB",
        size=(128, 128),
        color='black'
    )

    draw = ImageDraw.Draw(image)

    for i in range(10):
        random_X = random.randint()
        random_point = random.randint()
        line_xy = ((0, 0), (128, 128))
        draw.line(line_xy, fill="white")

        image.save("test_image.png")

if __name__ == "__main__":
    generate_art()