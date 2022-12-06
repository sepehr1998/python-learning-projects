import math

def calculate_square_area(length):
    return length*length


def calculate_sector_area(radius, angle):
    return (angle/360)*math.pi*radius**2

def calculate_catheti(hypo):
    return ((hypo**2)/2)**(1/2)

def calculate_figure_area(x):
    area1 = calculate_square_area(x)
    half_side = calculate_catheti(x)
    side = half_side*2
    area2 = (half_side**2)/2
    area3 = side**2
    area4 = calculate_sector_area(side, 270)
    area5 = calculate_sector_area(half_side, 45)
    return area1+area2+area3+area4+area5

new_x = float(input("Input x: "))
result = calculate_figure_area(new_x)
print("Figure area: " + str(round(result, 4)))
