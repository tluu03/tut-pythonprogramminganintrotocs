from graphics import *

def main():
    # Intro
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))

    # Create a graphics window w/ labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20,180), " 2.25K").draw(win)
    Text(Point(20, 80), " 7.5K").draw(win)
    Text(Point(20,30), " 10.0K").draw(win)

    # Draw bar for initial pricipal
    
    height = principal * 0.02
    bar = Rectangle(Point(40,230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for next year
        principal = principal * (1 + apr)

        # draw bar for this value
        xll = year * 25 + 40
        height = principal * .02
        bar = Rectangle(Point(xll, 230), Point(xll+ 25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()
