from PIL import Image, ImageDraw
import os


def drawRectangle(img, background_color, width, height, border_radius):
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        radius=border_radius,
        fill=background_color
    )
    
    return draw



def create_square_border(
    file_name="square_border",
    path="",
    width=256,
    height=256,
    border_radius=20,
    background_color = (255, 255, 255, 255),
):  
    # Create the directory if it does not exist
    os.makedirs(path, exist_ok=True)
    
    # Create square with border
    img = Image.new("RGBA", (width, height), (0,0,0,0))
    drawRectangle(img, background_color, width, height, border_radius)

    # Sauvegarder l'image
    img.save(os.path.join(path + file_name + ".png"))