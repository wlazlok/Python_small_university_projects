class Figure:
    def __init__(self, colour = "red", is_filled = True):
        self._colour = colour
        self._is_filled = is_filled
    def __str__(self):
        return "Kolor: " + self._colour + ", czy wybrany: " + str(self._is_filled)
    def __repr__(self):
        return f"colour = {self._colour}, is_filled(True/False) = {self._is_filled}"

#figura = Figure("niebieski", True)
#print(figura)
#print(figura.__repr__())

class Circle(Figure):
    def __init__(self,colour, is_filled, radius):
        Figure.__init__(self, colour, is_filled)
        self.radius = radius
    def __str__(self):
        return Figure.__str__(self) + ", radius: " + str(self.radius)
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Podana zla wartosc radius! (ustawiono wartosc domysla 90")
            self.__radius = 50
    def area(self):
        return "Pole kola = " + str(3.14 * self.radius * self.radius)
    def perimeter(self):
        return "Obwod kola = " + str(round(2 * 3.14 * self.radius, 2))
    def diametr(self):
        return f"Srednia kola {2 * self.radius}"
    def __repr__(self):
        return Figure.__repr__(self) + f" radius = {self.radius}"

#circle = Circle("zielony", False, 5)
#print(circle)
#print(circle.area())
#print(circle.perimeter())
#print(circle.diametr())
#print(circle.__repr__())

class Rectangle(Figure):
    def __init__(self, colour, is_filled, width, height):
        Figure.__init__(self, colour, is_filled)
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Podano zla szerokosc! (ustaawiono domysla wartosc 20)")
            self.__width = 20
    @property
    def height (self):
        return self.__height
    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Podano zla wysokosc! (ustawiono domyslna wartosc 50")
            self.__height = 50
    def __str__(self):
        return Figure.__str__(self) + f" szerokosc = {self.width}, wysokosc = {self.height}"
    def area(self):
        return f"Pole prostokata = {self.height * self.width}"
    def perimeter(self):
        return f"Obwod prostokata = {2 * self.width + 2 * self.height}"
    def __repr__(self):
        return Figure.__repr__(self) + f" szerokosc = {self.width}, wysokosc = {self.height}"

#prostokat = Rectangle("czerwony", True, 100, 200)
#print(prostokat)
#print(prostokat.area())
#print(prostokat.perimeter())
#print(prostokat.__repr__())