from src.models import *
from view.CONFIG import size
import src.functions as f
from view import utils

A = f.get_random_point(0, 0, size, size)
B = f.get_random_point(0, 0, size, size)
C = f.get_random_point(0, 0, size, size)

t = Triangle(A, B, C)
t.color = 'blue'
t.show()

colors = ['red', 'blue']
steps = 10
width = 1
k = 0.7

points = []
triangles = [t]

while steps:
    color = colors[steps % 2]

    new_pt = f.get_lemoine_point(triangles[-1])
    # new_pt = f.get_centroid_point(triangles[-1])
    # new_pt = f.get_incenter_point(triangles[-1])
    # new_pt = f.get_circumcenter_point(triangles[-1])
    # new_pt = f.get_np_center_point(triangles[-1])
    # new_pt = f.get_strange_point(triangles[-1], deg=-1)
    # new_pt = f.get_orthocenter_point(triangles[-1])
    new_pt.color = color
    # new_pt.show()

    new_tr = new_pt.project_on_triangle(triangles[-1])
    new_tr.color = color
    new_tr.border_width = width
    new_tr.init_ui()
    new_tr.show()

    points.append(new_pt)
    triangles.append(new_tr)
    width *= k
    steps -= 1


for i in range(len(triangles)):
    t = triangles[i]
    print(f'{t.s1.len()/t.s2.len()}; {t.s2.len()/t.s3.len()}; {t.s3.len()/t.s1.len()}')


filename = input('filename to save [press Enter if do not want to]:\n')
if filename != '':
    utils.save_viewport(filename=filename)
    print('saved successfully')
