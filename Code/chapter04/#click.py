#click.py
from graphics import *

def main():
    win = GraphWin("click me!")
    for i in range(10):
        P = win.getMouse()
        print("you clicked at:", p.getX(), p.getY())
        
        
