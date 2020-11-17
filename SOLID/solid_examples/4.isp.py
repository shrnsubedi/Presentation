
'''
I: Interface Segregation Principle

Many client-specific interfaces are better than one general-purpose interface.
or
Client must not be forced to implemet a method that it doesn't require.

'''

class IShape:
    def draw_shape(self):
        pass

class Circle(IShape):
    def draw_shape(self):
        radius

class Square(IShape):
    def draw_shape(self):
        widhth heght

class Rectangle(IShape):


class Triangle(IShape):
