#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 18:13:24 2025

@author: afok21
"""

from graphics import *
import math as m

def graphWin(Title):
    win = GraphWin(Title, 400, 400)
    win.setCoords(-10, -10, 10, 10)

    message = Text(Point(-0.1, 8), "Click to delineate points on the graph.")
    message.draw(win)

    axisX = Line(Point(-10, 0), Point(10, 0))
    axisX.draw(win)

    axisY = Line(Point(0, 10), Point(0, -10))
    axisY.draw(win)

    r = Rectangle(Point(-9, -9), Point(-7, -8))
    r.draw(win)

    rCenter = r.getCenter()
    stopMouse = Text(rCenter, "Done")
    stopMouse.draw(win)

    click = Point(0, 0)
    allPoints = []

    while True:
        click = win.getMouse()
        if (-9 <= click.getX() <= -7) and (-9 <= click.getY() <= -8):
            break
        else:
            allPoints.append(click)
            clickMarker = Circle(click, 0.1)
            clickMarker.setFill("blue")
            clickMarker.draw(win)

    return allPoints, win

def average(allPoints):
    sumX = 0
    sumY = 0
    count = 0
    sumXiYi = 0
    sumSqXi = 0
    sumSqYi = 0

    for i in allPoints:
        x = i.getX()
        y = i.getY()
        sumX += x
        sumY += y
        count += 1
        xy = x * y
        sumXiYi += xy
        SqX = x * x
        sumSqXi += SqX
        SqY = y * y
        sumSqYi += SqY

    a = ((sumY * sumSqXi) - (sumX * sumXiYi)) / (count * sumSqXi - sumX ** 2)
    b = ((count * sumXiYi) - (sumX * sumY)) / (count * sumSqXi - sumX ** 2)

    return a, b

def main():
    allPoints, win = graphWin("Regression Line")
    if len(allPoints) < 2:
        message = Text(Point(0, 0), "At least two points are required.")
        message.setFill("red")
        message.draw(win)
        win.getMouse()
        win.close()
        return

    a, b = average(allPoints)
    x1 = -10
    x2 = 10
    y1 = a + b * x1
    y2 = a + b * x2

    regressLine = Line(Point(x1, y1), Point(x2, y2))
    regressLine.setFill("red")
    regressLine.setWidth(2)
    regressLine.draw(win)

    win.getMouse()
    win.close()

main()