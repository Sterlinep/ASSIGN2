import turtle


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        for i in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


if __name__ == '__main__':
    p = Point(100, 100, 'red')
    p.draw()
    b = Box(10, 20, 50, 100, 'green')
    b.draw()
    bf = BoxFilled(-100, 20, 50, 100, 'green', 'blue')
    bf.draw()
    c = Circle(300, 150, 50, 'black')
    c.draw()
    cf = CircleFilled(-300, 150, 50, 'red', 'yellow')
    cf.draw()
    turtle.hideturtle()
    turtle.done()
#same code with comments, for learning

import turtle


# Point class
class Point(object):
    # constructor taking x, y and color
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # method to adjust turtle and position, then draws the point
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    # method that actually draws the point
    def draw_action(self):
        turtle.dot()


# Box class inherited from Point
class Box(Point):
    # constructor taking x,y,width,height and color
    def __init__(self, x1, y1, width, height, color):
        # passing x,y and color to Point class constructor
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        # looping for 2 times
        for i in range(2):
            # moving forward width spaces, turning right
            turtle.forward(self.width)
            turtle.right(90)
            # moving forward height spaces, turning right
            turtle.forward(self.height)
            turtle.right(90)


# BoxFilled class inherited from Box class
class BoxFilled(Box):
    # constructor taking x,y, width, height, color and fillcolor
    def __init__(self, x1, y1, width, height, color, fillcolor):
        # passing x,y,width,height and color to super class
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        # setting fill color
        turtle.fillcolor(self.fillcolor)
        # beginning fill
        turtle.begin_fill()
        # calling draw_action of Box class
        Box.draw_action(self)
        # finishing fill
        turtle.end_fill()


# Circle class inherited from Point
class Circle(Point):
    # constructor taking x,y, radius and color
    def __init__(self, x1, y1, radius, color):
        # passing x,y and color to super class
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        # simply drawing circle with stored radius
        turtle.circle(self.radius)


# CircleFilled class inherited from Circle
class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        # setting fill color
        turtle.fillcolor(self.fillcolor)
        # beginning fill
        turtle.begin_fill()
        # performing draw_action of Circle class
        Circle.draw_action(self)
        # finishing fill
        turtle.end_fill()


# code for testing
if __name__ == '__main__':
    # creating and drawing a red point
    p = Point(100, 100, 'red')
    p.draw()
    # creating and drawing a green outlined box
    b = Box(10, 20, 50, 100, 'green')
    b.draw()
    # creating and drawing a green outlined box filled with blue
    bf = BoxFilled(-100, 20, 50, 100, 'green', 'blue')
    bf.draw()
    # creating and drawing a black outlined circle
    c = Circle(300, 150, 50, 'black')
    c.draw()
    # creating and drawing a black outlined circle with yellow fill
    cf = CircleFilled(-300, 150, 50, 'red', 'yellow')
    cf.draw()
    # hiding turtle and finishing drawing
    turtle.hideturtle()
    turtle.done()