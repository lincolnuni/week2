class circle:
    def findcircumference(self, radius):
        return 2 * 3.14159 * radius
        
    def  findAreaofCircle(self, radius):
        return  3.14159 * radius**2

print("Enter the Radius = ", end= "")

r = float(input())
ob = circle()
c = ob.findcircumference(r)
a = ob.findAreaofCircle(r)
d = c + a

print("\n Area of a Circumference =  {:.2f}".format(d))
print(" Area of a Circle =  {:.2f}".format(a))


