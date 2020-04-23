class coordinate:
    x = 0
    y = 0

p1 = coordinate()
p2 = coordinate()
p1.x = 3
p1.y = 3
p2.x = 2
p2.y = 2
def func1(point1,point2):
    return(((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5)
