class Circle:
    def __init__(self,pi,radius):
        self.pi=pi
        self.radius=radius
    def display(self):
        area=pi*radius*radius
        print("The area of circle is: ",area)

pi=3.14
radius=int(input("Enter radius of circle: "))
c1=Circle(pi,radius)
cl.display()
