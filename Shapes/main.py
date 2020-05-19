import figure_module as fig

figura = fig.Figure("niebieski", True)
print(figura)
print(figura.__repr__())

circle = fig.Circle("zielony", False, 5)
print(circle)
print(circle.area())
print(circle.perimeter())
print(circle.diametr())
print(circle.__repr__())

prostokat = fig.Rectangle("czerwony", True, 100, 200)
print(prostokat)
print(prostokat.area())
print(prostokat.perimeter())
print(prostokat.__repr__())