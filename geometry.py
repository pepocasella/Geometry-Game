import math
import turtle

class Point:

    def __init__(self, x_value, y_value):
        '''
        Method to declare what instance variables this object will have.
        '''
        # instance variables
        self.x = x_value # x -> attribute from the Point Class
        self.y = y_value # y_value -> argument value
         
    def falls_in_rectangle(self, ractangle):
        '''
        Class method to check if the point is inside a given rectangle.
        '''
        if  ractangle.point1.x < self.x < ractangle.point2.x \
            and ractangle.point1.y < self.y < ractangle.point2.y:
            return True 
        else:
            return False

    def calculate_distance(self, point):
        '''
        Class method to calculate a distance from the objet point to a new
        given point.
        '''
        distance = math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
        return distance


class Rectangle:
 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
 
    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)



class GuiRectangle(Rectangle):
    '''
    Graph User Interface to draw the rectangle

    GuiRectangle Class inheriting from the Rectangle Class. It inherits
    the instances variables like points and also the methods from the 
    inheriting Rectangle Class
    '''

    def draw(self, canvas):
        '''
        Class method to draw the rectangle o the screen
        '''
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y) # Turn turtle by 90 degree
        canvas.pendown()

        # drawing first side
        canvas.forward(self.point2.x - self.point1.x) # Forward turtle by l units
        canvas.left(90) # Turn turtle by 90 degree

        # drawing second side
        canvas.forward(self.point2.y - self.point1.y) # Forward turtle by w units
        canvas.left(90) # Turn turtle by 90 degree
        
        # drawing third side
        canvas.forward(self.point2.x - self.point1.x) # Forward turtle by l units
        canvas.left(90) # Turn turtle by 90 degree
        
        # drawing fourth side
        canvas.forward(self.point2.y - self.point1.y) # Forward turtle by w units
        canvas.left(90) # Turn turtle by 90 degree




class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)



 

