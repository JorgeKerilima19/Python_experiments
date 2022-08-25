#WIth a circle radio of 1 inside a square we can calculate PI, by drawing random points and messuring them to the center
#The distance between two points is determine by the sum of the square of x and Y
#if the result is greater than 1 it is outside the circle, otherwise, it is inside
# the area of a circle is determine by PI*square r and the square area is 2rsquare
#this leads us to (PI*(R**2))/(2*R)**2= N.pointsInsideCircle/N.pointsTotal where R equals 1
#simplifying our formula becomes PI=4(PointInside)/PointTotal

import random

def PI(n):
    points_inside=0
    points_total=0
    for i in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        dstance=x**2+y**2
        if dstance<=1:
            points_inside+=1
        points_total+=1
    return 4*points_inside/points_total

print(PI(550))