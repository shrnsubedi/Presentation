
'''
S: Single Responsibility Principle

“Every module/class should only have one responsibility and therefore only one reason to change.”

Single Responsibility allows for increased cohesion and reduced coupling because any given responsibility 
is in a single place and don’t overlap.
'''

#Unfactored:

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width 
        self.height = height

    def area(self):
        return self.width * self.height
    
    def draw(self):
        canvas.draw(x_cord,_y_cord,self.width,self.height)
        pass

#-------->
#Refactored
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width 
        self.height = height
        rectangleui=RectangleUI()

    def area(self):
        return self.width * self.height
    
    def draw():
        rectangleui.draw()
    

class RectangleUI:
    def get_rectangle():
        rectangle=Rectanle(5,5)

    def draw(self):
        canvas.draw(x_cord,_y_cord,self.width,self.height)
        pass
