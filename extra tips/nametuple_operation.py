from collections import namedtuple

# more readable and immutable like tuple

Color = namedtuple('Color', ['red','green','blue'])

color = Color(55,155,255)
white = Color(255,255,255)
print(color.red)
print(color)
print(white.red)