from src.models import *


def get_random_point(x_min: int, y_min: int, x_max: int, y_max: int):
    import random

    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)

    return Point(x, y)


def get_lemoine_point(t: Triangle):
    w1 = t.s1.squared_len()
    w2 = t.s2.squared_len()
    w3 = t.s3.squared_len()

    return t.bar_point(w1, w2, w3)


def get_centroid_point(t: Triangle):
    return t.bar_point(1, 1, 1)


def intersection(line_1, line_2):
    p1, p2 = line_1.p1, line_1.p2

    proj_1 = p1.project_on(line_2)
    proj_2 = p2.project_on(line_2)

    d1 = p1.signed_dist_to(line_2)
    d2 = -p2.signed_dist_to(line_2)

    return proj_1 * (d2/(d1 + d2)) + proj_2 * (d1/(d1 + d2))


def get_incenter_point(t: Triangle):
    # using bisector theorem
    len_1, len_2, len_3 = t.s1.len(), t.s2.len(), t.s3.len()

    b3 = t.v1 * (len_1 / (len_1 + len_2)) + t.v2 * (len_2 / (len_1 + len_2))
    b2 = t.v1 * (len_1 / (len_1 + len_3)) + t.v3 * (len_3 / (len_1 + len_3))

    incenter = intersection(Segment(t.v3, b3), Segment(t.v2, b2))
    return incenter


def get_circumcenter_point(t: Triangle):
    # calculating intersection of median perpendiculars
    b3 = t.v1 * 0.5 + t.v2 * 0.5
    b2 = t.v1 * 0.5 + t.v3 * 0.5

    h3 = b3 + t.s3.normal()
    h2 = b2 + t.s2.normal()

    circumcenter = intersection(Segment(b3, h3), Segment(b2, h2))
    return circumcenter


def get_np_center_point(t: Triangle):
    sq_1, sq_2, sq_3 = t.s1.len()**2, t.s2.len()**2, t.s3.len()**2

    n1 = sq_1 * (sq_2 + sq_3) - (sq_2 - sq_3) ** 2
    n2 = sq_2 * (sq_1 + sq_3) - (sq_1 - sq_3) ** 2
    n3 = sq_3 * (sq_2 + sq_1) - (sq_2 - sq_1) ** 2

    return t.bar_point(n1, n2, n3)


def get_strange_point(t: Triangle, deg):
    d_1, d_2, d_3 = t.s1.len() ** deg, t.s2.len() ** deg, t.s3.len() ** deg
    d = d_1 + d_2 + d_3
    print(d)

    strange_point = t.v1 * (d_1/d) + t.v2 * (d_2/d) + t.v3 * (d_3/d)
    return strange_point


def get_orthocenter_point(t: Triangle):
    # todo: add new definition using tangents
    p1 = t.v1.project_on(t.s1)
    p2 = t.v2.project_on(t.s2)

    h1 = Segment(t.v1, p1)
    h2 = Segment(t.v2, p2)

    return intersection(h1, h2)









