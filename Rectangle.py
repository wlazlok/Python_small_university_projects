
class Rectangle:
    length = 0
    height = 0

    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self):
        return 'length=' + str(self.length) + ', height=' + str(self.height)

    def __repr__(self):
        return f"Height: {self.height}, Length: {self.length}."


class Cuboid(Rectangle):
    width = 0

    def __init__(self, length, height, width):
        Rectangle.length = length
        Rectangle.height = height
        self.width = width

    def area(self):
        return 2 * (Rectangle.area(self) + (Rectangle.height * self.width) + (Rectangle.length * self.width))

    def __str__(self):
        return 'Rectangle(length=' + str(Rectangle.length) + ', heigth=' + str(Rectangle.height) + ', width=' + str(
            self.width) + ')'

    def capacity(self):
        return Rectangle.area(self) * self.width

    def __repr__(self):
        return f"Width: {self.width}, Height: {Rectangle.height}, Length: {Rectangle.length}."




class InvalidData(Exception):
    pass

def open_file(fileName):
    with open(fileName) as f:
        line1 = f.readline().split()
        line2= f.readline().split()

        try:
            controlSum = 0
            for index in line1:
                if int(index) > 0:
                    controlSum += 1
                elif int(index) <= 0:
                    raise InvalidData
                    break
        except InvalidData:
            print("Invalid value!\nA rectangle will not be created")


        if int(line1[0]) == 1 and controlSum == 3:
            print("[1] Rectangle:")
            obj = Rectangle(int(line1[1]), int(line1[2]))
            print(obj.__repr__())
            print("Area: " + str(obj.area()) + "\n")

        try:
            controlSum = 0
            for index in line2:
                if int(index) > 0:
                    controlSum += 1
                elif int(index) <= 0:
                    raise InvalidData
                    break
        except InvalidData:
            print("Invalid value!\nA cuboid will not be created...")


        if int(line2[0]) == 2 and controlSum == 4:
            print("[2] Cuboid:")
            obj = Cuboid(int(line2[1]), int(line2[2]), int(line2[3]))
            print(obj.__repr__())
            print("Capacity: " + str(obj.capacity()) + ", Area: " + str(obj.area()))

open_file('ab.txt')






