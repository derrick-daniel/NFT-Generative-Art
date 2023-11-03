from PIL import Image

def generate_art():
    image = Image.new(
        mode="RGB",
        size=(128, 128),
        color='black'
    )
    image.save("test_image.png")

if __name__ == "__main__":
    generate_art()