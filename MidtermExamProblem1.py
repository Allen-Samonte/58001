class Circle():
    def radius(self,radius):
        radius = radius
    def diameter(self,radius):
        diameter = 2*radius
        print("The Diameter of the circle is: ",diameter)
    def area(self,radius):
        area = round(3.142*radius*radius, 2)
        print("The Area of the circle is: ",area)
    def perimeter(self,radius):
        perimeter = round(2*3.14*radius, 2)
        print("The Perimeter of the circle is: ",perimeter)

circle = Circle()
radius = int(input("Please enter the radius of circle: "))
circle.diameter(radius)
circle.area(radius)
circle.perimeter(radius)