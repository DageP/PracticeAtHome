class triangle(object): #"Method" is essentially a function inside a class
    number_of_sides = 3

    def __init__(self, Angle1, Angle2, Angle3): #Self would act as a container to store the value 
        self.Angle1 = Angle1
        self.Angle2 = Angle2
        self.Angle3 = Angle3

    def check_angles(self):
        Sum = self.Angle1 + self.Angle2 + self.Angle3 #It can be passed to the next method
        if Sum == 180:
            return True
        else:
            return False

    def triangle_type(self):
        Angles = []
        Angles.append(self.Angle1)
        Angles.append(self.Angle2)
        Angles.append(self.Angle3)
        for i in Angles:
            if i == 90:
                return "The triangle is a right-angled triangle"
            elif Angles[0] == Angles[1] == Angles[2]:
                return "The triangle is an equilateral triangle"
            elif Angles[0] == Angles[1] or Angles[0] == Angles[2] or Angles[2] == Angles[1]:
                return "The triangle is an isosceles triangle"
            else:
                return "The triangle is a scalene triangle"

my_triangle = triangle(60,60,60)
print("The number of sides of a triangle is : ", my_triangle.number_of_sides)
print(my_triangle.check_angles())
print(my_triangle.triangle_type())
