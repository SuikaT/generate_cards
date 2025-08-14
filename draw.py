from PIL import Image, ImageDraw
import os
import math

def drawCard(img, background_color, width, height, corner_radius):
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        radius=corner_radius,
        fill=background_color
    )
    
    return draw

def create_card_with_circle(
    circle_color = (255, 255, 0, 255),
    file_name="card_circle",
    path="",
    circle_diameter=350,
    background_color = (238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20,
):  
    # Create the directory if it does not exist
    os.makedirs(path, exist_ok=True)
    
    # Créer l'image avec fond coloré
    img = Image.new("RGBA", (width, height), (0,0,0,0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Ajouter un cercle jaune centré de 70px de diamètre
    top_left = ((width - circle_diameter) // 2, (height - circle_diameter) // 2)
    bottom_right = (top_left[0] + circle_diameter, top_left[1] + circle_diameter)

    draw.ellipse([top_left, bottom_right], fill=circle_color)

    # Sauvegarder l'image
    img.save(os.path.join(path + file_name + ".png"))
    


def create_card_with_square(
    square_color = (255, 255, 0, 255),
    file_name="card_square",
    path="",
    square_size=350,
    background_color = (238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20,
):
    # Create the directory if it does not exist
    os.makedirs(path, exist_ok=True)
    
    # Créer l'image avec fond coloré
    img = Image.new("RGBA", (width, height), (0,0,0,0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Ajouter un cercle jaune centré de 70px de diamètre
    top_left = ((width - square_size) // 2, (height - square_size) // 2)
    bottom_right = (top_left[0] + square_size, top_left[1] + square_size)

    # Draw the centered square
    draw.rectangle([top_left, bottom_right], fill=square_color)

        # Sauvegarder l'image
    img.save(os.path.join(path + file_name + ".png"))
    
    
def create_card_with_hexagon(
    hexagon_color = (255, 255, 0, 255),
    file_name="card_hexagon",
    path="",
    hexagon_size=350,
    background_color = (238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20,
):
    # Create the directory if it does not exist
    os.makedirs(path, exist_ok=True)
    
    # Créer l'image avec fond coloré
    img = Image.new("RGBA", (width, height), (0,0,0,0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Center coordinates
    cx = width / 2
    cy = height / 2

    # Radius from center to any vertex
    radius = hexagon_size / 2

    # Calculate the 6 vertices of the hexagon
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30  # flat-top hexagon
        angle_rad = math.radians(angle_deg)
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        points.append((x, y))

    # Draw the centered hexagon
    draw.polygon(points, fill=hexagon_color)

        # Sauvegarder l'image
    img.save(os.path.join(path + file_name + ".png"))
    
    
def create_card_with_octagon(
    octagon_color=(255, 255, 0, 255),
    file_name="card_octagon",
    path="",
    octagon_size=350,  # distance entre deux côtés opposés
    background_color=(238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20,
):
    # Créer le dossier si inexistant
    os.makedirs(path, exist_ok=True)

    # Créer l'image
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Centre
    cx = width / 2
    cy = height / 2

    # Rayon (centre → sommet)
    radius = octagon_size / 2

    # Calcul des 8 sommets
    points = []
    for i in range(8):
        angle_deg = 45 * i  # 360/8 = 45°
        angle_rad = math.radians(angle_deg)
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        points.append((x, y))

    # Dessiner l'octogone centré
    draw.polygon(points, fill=octagon_color)

    # Sauvegarde
    img.save(os.path.join(path, file_name + ".png"))
    
    
def create_card_with_triangle(
    triangle_color=(255, 255, 0, 255),
    file_name="card_triangle",
    path="",
    triangle_size=350,
    background_color=(238, 238, 228, 255),
    width=420,
    height=560,
    corner_radius=20,
):
    # Créer le dossier si inexistant
    os.makedirs(path, exist_ok=True)

    # Créer l'image
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = drawCard(img, background_color, width, height, corner_radius)

    # Centre de la carte
    cx = width / 2
    cy = height / 2

    # Coordonnées du sommet du triangle (haut)
    radius = triangle_size / math.sqrt(3)  # pour un triangle équilatéral

    # Calcul des 3 sommets (rotation pointy-top)
    points = []
    for i in range(3):
        angle_deg = 120 * i - 90  # sommet vers le haut
        angle_rad = math.radians(angle_deg)
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        points.append((x, y))

    # Dessiner le triangle
    draw.polygon(points, fill=triangle_color)

    # Sauvegarde
    img.save(os.path.join(path, file_name + ".png"))