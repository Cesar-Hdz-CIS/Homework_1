# Cesar Hernandez 1835494
import math

wall_height = float(input('Enter wall height (feet):\n'))
wall_width = float(input('Enter wall width (feet):\n'))
wall_area = wall_width*wall_height
coverage = 350

print('Wall area:', int(wall_area), "square feet")
print('Paint needed:', '{:.2f}'.format(wall_area/coverage), 'gallons')
print('Cans needed:', math.ceil(wall_area/coverage), 'can(s)')

colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

color = input('\nChoose a color to paint the wall:\n')

per_can = colors[color]*(math.ceil(wall_area/coverage))

print('Cost of purchasing', color, 'paint: $' + str(per_can))