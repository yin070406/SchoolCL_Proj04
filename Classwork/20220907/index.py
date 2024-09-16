"""

?<!DOCTYPE html>
    <head>
*        <link rel="name" href="Ng Tsz Yin".css>
    </head>

    <div class="class">
*        4B
    </div>

    <div class="class_number">
*        12
    </div>

?</html>

"""

import math

radius = float(input("Please the Radius of the Sphere: "))

#Define cube = r * r * r, which mean = r**3
def cube(radius):
    return radius * radius * radius

volume = 4/3 * math.pi * cube(radius)

print(volume)