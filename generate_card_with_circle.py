from PIL import Image, ImageDraw

def create_square_with_circle(
    circle_color = (255, 255, 0, 255),
    circle_diameter=250,
    background_color = (238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20
):
    # Créer l'image avec fond coloré
    img = Image.new("RGBA", (width, height), (0,0,0,0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Ajouter un cercle jaune centré de 70px de diamètre
    top_left = ((width - circle_diameter) // 2, (height - circle_diameter) // 2)
    bottom_right = (top_left[0] + circle_diameter, top_left[1] + circle_diameter)

    draw.ellipse([top_left, bottom_right], fill=circle_color)

    # Sauvegarder l'image
    img.save("card_yellow_circle.png")

def drawCard(img, background_color, width, height, corner_radius):
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        radius=corner_radius,
        fill=background_color
    )
    
    return draw
    
    
create_square_with_circle()