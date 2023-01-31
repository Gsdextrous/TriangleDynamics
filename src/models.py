from fractions import Fraction
from view.viewport import plot
from src import utils as u


class BaseModel:
    def __init__(self):
        self.plot = plot
        self.name = ''
        self.color = 'black'


class Point(BaseModel):
    def __init__(self, _x: float, _y: float):
        super().__init__()
        self.x = Fraction(_x).limit_denominator()
        self.y = Fraction(_y).limit_denominator()
        self.tuple = (float(self.x), float(self.y))

    def __str__(self):
        return f"Point{self.tuple}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other: float):
        return Point(self.x * other, self.y * other)

    # scalar product
    def __and__(self, other):
        return self.x * other.x + self.y * other.y

    # 'vector' product
    def __xor__(self, other):
        return self.x * other.y - self.y * other.x

    def norm(self):
        import math
        return math.sqrt(float(self.x ** 2 + self.y ** 2))

    def squared_norm(self):
        return float(self.x ** 2 + self.y ** 2)

    def signed_dist_to(self, line):
        n = line.normal()
        v = self - line.p1
        signed_dist = (n & v) / (n & n) ** 0.5

        return signed_dist

    def dist_to(self, line):
        return abs(self.signed_dist_to(line))

    def project_on(self, line):
        n = line.normal()
        v = self - line.p1
        v_proj = v - n * ((n & v)/(n & n))
        p_proj = line.p1 + v_proj

        return p_proj

    def project_on_triangle(self, triangle):
        p1 = self.project_on(triangle.s1)
        p2 = self.project_on(triangle.s2)
        p3 = self.project_on(triangle.s3)

        return Triangle(p1, p2, p3)

    def show(self):
        plt = self.plot
        x, y = float(self.x), float(self.y)

        plt.add(plt.circle(
            center=(x, y),
            r=2,
            fill=self.color
        ))
        plt.add(plt.text(
            text=self.name,
            insert=(x, y),
            style=u.font_style(10)
        ))
        plt.save()


class Line(BaseModel):
    def __init__(self, _p1: Point, _p2: Point):
        super().__init__()
        self.p1 = _p1
        self.p2 = _p2


class Segment(BaseModel):
    def __init__(self, _p1: Point, _p2: Point):
        super().__init__()
        self.width = 1
        self.p1 = _p1
        self.p2 = _p2

    def show(self):
        plt = self.plot

        plt.add(plt.line(
            start=self.p1.tuple,
            end=self.p2.tuple,
            stroke=self.color,
            style=f"stroke-width: {self.width}"
        ))
        plt.save()

    def len(self):
        return (self.p1 - self.p2).norm()

    def squared_len(self):
        return (self.p1 - self.p2).squared_norm()

    def dir_vector(self):
        return Point(self.p2.x - self.p1.x, self.p2.y - self.p1.y)

    def normal(self):
        return Point(self.p1.y - self.p2.y, self.p2.x - self.p1.x)


class Triangle(BaseModel):
    def __init__(self, _v1: Point, _v2: Point, _v3: Point):
        super().__init__()
        self.opacity = '0.20'
        self.border_width = 1
        self.v1 = _v1
        self.v2 = _v2
        self.v3 = _v3

        self.l1 = Line(self.v2, self.v3)
        self.l2 = Line(self.v1, self.v3)
        self.l3 = Line(self.v1, self.v2)

        self.s1 = Segment(self.v2, self.v3)
        self.s2 = Segment(self.v1, self.v3)
        self.s3 = Segment(self.v1, self.v2)

        self.init_ui()

    def init_ui(self):
        # self.l1.width = self.border_width
        # self.l2.width = self.border_width
        # self.l3.width = self.border_width

        self.s1.width = self.border_width
        self.s2.width = self.border_width
        self.s3.width = self.border_width

    def bar_point(self, b1, b2, b3):    # point in (unnormalized) barycentric coordinates
        b_sum = b1 + b2 + b3
        return self.v1 * (b1 / b_sum) + self.v2 * (b2 / b_sum) + self.v3 * (b3 / b_sum)

    def show(self):
        # recursively showing simplexes of lower dimensions
        # self.v1.show()
        # self.v2.show()
        # self.v3.show()

        self.s1.show()
        self.s2.show()
        self.s3.show()

        plt = self.plot
        plt.add(plt.polygon(
            points=[self.v1.tuple, self.v2.tuple, self.v3.tuple],
            fill=self.color,
            opacity=self.opacity
        ))
        plt.save()


