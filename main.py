from draw import *

colors = [[(245, 73, 39, 255), "orange"], [(123, 199, 119, 255), "green"], [(119, 199, 187, 255), "turquoise"], [(119, 124, 199, 255), "blue"], [(180, 119, 199, 255), "violet"], [(219, 53, 81, 255), "red"]]


for i, color in enumerate(colors):
    circleFileName = "card_" + color[1] + "_circle_"
    create_card_with_circle(color[0], circleFileName + str(350), "cards/circle_350/", 350)
    
    create_card_with_circle(color[0], circleFileName + str(300), "cards/circle_300/", 300)
    
    
    squareFileName = "card_" + color[1] + "_square_"
    create_card_with_square(color[0], squareFileName + str(300), "cards/square_300/", 300)
    
    create_card_with_square(color[0], squareFileName + str(250), "cards/square_250/", 250)
    
    hexagonFileName = "card_" + color[1] + "_hexagon_"
    create_card_with_hexagon(color[0], hexagonFileName + str(300), "cards/hexagon_300/", 300)
    
    create_card_with_hexagon(color[0], hexagonFileName + str(250), "cards/hexagon_250/", 250)
    
    octagonFileName = "card_" + color[1] + "_octagon_"
    create_card_with_octagon(color[0], octagonFileName + str(300), "cards/octagon_300/", 300)
    
    create_card_with_octagon(color[0], octagonFileName + str(250), "cards/octagon_250/", 250)
    
    triangleFileName = "card_" + color[1] + "_triangle_"
    create_card_with_triangle(color[0], triangleFileName + str(300), "cards/triangle_300/", 300)
    
    create_card_with_triangle(color[0], triangleFileName + str(250), "cards/triangle_250/", 250)