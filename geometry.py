

class Point:

    def __init__(self, x_value, y_value):
        '''
        Method to declare what instance variables this object will have
        '''
        # instance variables
        self.x = x_value # x -> attribute from the Point Class
        self.y = y_value # y_value -> argument value
         
    def falls_in_rectangle(self, lowleft, upright):
        '''
        Class method to check if the point is inside a given rectangle
        '''
        if lowleft[0] < self.x < upright[0] \
            and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False


point_1 = Point(1, 2) # instantiating a class -> creating an object
print(point_1, type(point_1), point_1.falls_in_rectangle((6,6), (9,9)))
