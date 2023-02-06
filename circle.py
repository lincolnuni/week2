class circle:
    def findAreaofCircle(self, radius):
        return 2 * 3.14159 * radius
print("Enter the Radius = ", end= "")

r = float(input())
ob = circle()
c = ob.findAreaofCircle(r)

# class cirncumference:
    # def Fincircumference(self, radius):
print("\n Area of a Circle =  {:.2f}".format(c))

