import math
x1,y1=input("Enter x and y location of Point1 : ").split()
x2,y2=input("Enter x and y location of Point2 : ").split()
distance=math.sqrt(((int(x2)-int(x1))*2)+((int(y2)-int(y1))*2))
dis=round((distance),2)
print("Distance between Points (",x1,",",y1,") and (",x2,",",y2,") : ",str(dis))