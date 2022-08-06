import math
from tkinter import Y

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
        if  ractangle.lowleft.x < self.x < ractangle.upright.x \
            and ractangle.lowleft.y < self.y < ractangle.upright.y:
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


class Rectangule:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

 

