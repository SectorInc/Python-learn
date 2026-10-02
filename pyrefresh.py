#  FUNCTIONS

#1)Pythogras Theorem
a=int(input("Enter height : "))
b=int(input("Enter width : "))
py=(pow(a,2) + b ** 2) **(0.5)
print(round(py,2))


#2) Area of a Right-Angled Triangle
base=int(input("Enter triangle base : "))
height=int(input("Enter triangle height : "))
triangle_area=base * height/2
print(triangle_area)

#3) Checking for a Pythagorean Triple
a=int(input("Enter height : "))
b=int(input("Enter width : "))
c=int(input("Enter pythogras : "))
if pow(a,2) + pow(b,2) == pow(c,2):
    print(True)
else:
    print(False)

#4)Distance Between Two 2D Points
x1=int(input("Enter distance : "))
x2=int(input("Enter distance : ")) 
cal_distanceX=x2-x1
print(cal_distanceX)
y1=int(input("Enter distance : "))
y2=int(input("Enter distance : "))
cal_distanceY=y2-y1
print(cal_distanceY)
Distance=pow(cal_distanceX,2) + pow(cal_distanceY,2)
print(Distance)
Distance=pow(Distance,0.5)
print(Distance)