import svgwrite
from view.CONFIG import size

plot = svgwrite.Drawing('view/plot.svg', size=(f'{size}', f'{size}'))

