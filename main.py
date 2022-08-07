import random
import turtle

from geometry import Point, Rectangle, GuiRectangle, GuiPoint

def main():
    
    # Generating Rectangle
    point_1  = Point(random.randint(0, 400), random.randint(0, 400))
    point_2  = Point(random.randint(10, 400), random.randint(10, 400))
    rectangle = GuiRectangle(point_1, point_2) # Random Rectangle

    print(f'''
    {'-'*25}
    Rectangle Coordinates: \n
    X1: {rectangle.point1.x}, Y1: {rectangle.point1.y} and X2: {rectangle.point2.x}, Y2: {rectangle.point2.y}
    {'-'*25}
    ''')

    # User's input
    user_point = GuiPoint(float(input('Guess X: ')), float(input('Guess Y: ')))
    user_area = float(input('Guess rectangle area: '))

    # Print all results
    print(f'Is the inputed point in the random rectangle?: {user_point.falls_in_rectangle(rectangle)}')
    print(f'Your guessed area was off by: {rectangle.area() - user_area}')

    myturtle = turtle.Turtle()
    rectangle.draw(canvas=myturtle)
    user_point.draw(canvas=myturtle)
    turtle.done()

if __name__ == '__main__':
    main()