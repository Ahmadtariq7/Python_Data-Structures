#           classes
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"


# creating instance without parameters
p1 = Point()
print("The value at x is:", p1.x, "And Value at y is:", p1.y)
# creating instance with parameters
p2 = Point(3, 4)
print("The value at x is:", p2.x, "And Value at y is:", p2.y)
print(p2)  # see result, it's coz of Dunder Function __str__


#           Composition
class Shape:
    def __init__(self, points):
        self.points = points

    def __str__(self):
        ret = ""
        for i in self.points:
            ret += str(i) + " - "
        return ret


p1 = Point(5, 5)
p2 = Point(10, 5)
p3 = Point(5, 10)
p = [p1, p2, p3]

sh = Shape(p)
print(sh)


# we can add function in class at runtime too..
def print_points(self):
    for i in self.points:
        print(i)


Shape.print_points = print_points
print("Points are: ")
sh.print_points()


#           Inheritance
class Triangle(Shape):
    pass


t = Triangle(p)
print("Triangle Points are: ")
t.print_points()


def get_area(self):
    vertices = self.points
    n = len(vertices)
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += abs(vertices[i].x * vertices[j].y - vertices[j].x * vertices[i].y)
        return a / 2.0


Triangle.get_area = get_area  # no parentheses
print("The area of Triangle is: ", t.get_area())


#           Access Parent Class' Overridden Methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def __str__(self):
        return "L: " + str(self.length) + " W: " + str(self.width)


rect = Rectangle(2, 4)
print(rect)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,
                         length)  # it will write length length instead of length, width.. coz square has same length each sides..

    def __str__(self):
        return "Square: " + super().__str__()


square = Square(4)
print(square.area())
print(square)
