from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def falls_in_rectangle(self, rectangle):
        if (rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y):
            return True
        else:
            return False

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self, rectangle):
        return (rectangle.upright.x - rectangle.lowleft.x) * (rectangle.upright.y - rectangle.lowleft.y)



point1 = Point(int(input("Enter x: ")), int(input("Enter y: ")))


rectangle = Rectangle(Point(randint(1,9), randint(1,9)), Point(randint(10,20), randint(10,20)))



print("Attributes of the rectangle are ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

print(point1.falls_in_rectangle(rectangle))