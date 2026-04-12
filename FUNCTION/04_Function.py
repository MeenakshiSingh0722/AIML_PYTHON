# area and circumference of circle
import math
def circle(r):
    a=math.pi* r**2
    c=2*math.pi*r
    return a,c

a,c=circle(4)
print("area: ",a," circumference: ",c)