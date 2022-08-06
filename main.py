import random

from geometry import Point, Rectangule

def main():
    
    # Generating Rectangle
    point_1  = Point(random.randint(0, 9), random.randint(0, 9))
    point_2  = Point(random.randint(10, 19), random.randint(10, 19))
    rectangle = Rectangule(point_1, point_2) # Random Rectangle

    print(f'''
    {'-'*25}
    Rectangle Coordinates: \n
    X1: {rectangle.lowleft.x}, Y1: {rectangle.lowleft.y} and X2: {rectangle.upright.x}, Y2: {rectangle.upright.y}
    {'-'*25}
    ''')

    # User's input
    user_point = Point(float(input('Guess X: ')), float(input('Guess Y: ')))
    print(f'Is the inputed point in the random rectangle?: {user_point.falls_in_rectangle(rectangle)}')

if __name__ == '__main__':
    main()
