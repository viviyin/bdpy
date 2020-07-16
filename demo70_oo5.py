class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(3, 5)
print(f'r1 size={r1.calculate_area()}')
r2 = Rectangle(4, 6)
print(f"r2 size={r2.calculate_area()}")
