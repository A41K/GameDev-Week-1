define Abigel = Character("Abigel", color="#f5ff69")
define James = Character("James", color="#69f5ff")
define N = Character("Narator", color="#808080")

default progression_points = 0

image nroom:
    "images/narator_room.webp"
    zoom 2

image outside:
    "images/outsidebig.jpg"
    zoom 3

image abigel happy:
    "images/outside.jpg"
    zoom 1

image james happy:
    "images/outside.jpg"
    zoom 1

label start:
    scene nroom

    N "There was once a beautiful time in a beautiful place. two people who seem far away started closing in the distance"

    N "You could feel the spark in their eyes. It could light a whole forest on fire, but it wasn't always like that"

    scene outside

    show james happy at center

    James "You know It's beautiful outside isn't it?" 

    hide james happy

    show abigel happy at center

    Abigel "Yes, it is. I love the smell of the flowers and the sound of the birds. It's so peaceful here."

    hide abigel happy

    James "Y'know I felt more peace everytime when we were here, together then elsewhere."
    James "It's like nature is more greener because of us."



    return