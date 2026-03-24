class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width: float):
        self._width = new_width
    
    @height.setter
    def height(self, new_height: float):
        self._height = new_height
    
    def set_width(self, new_width: float):
        self.width = new_width
    
    def set_height(self, new_height: float):
        self.height = new_height
    
    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(int(self.height)):
            picture += "*" * int(self.width) + "\n"
        return picture
    
    def get_amount_inside(self, shape) -> int:
        return int(self.get_area() // shape.get_area())
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length: float):
        super().__init__(side_length, side_length)
    
    def set_width(self, new_width: float):
        self._width = new_width
        self._height = new_width
    
    def set_height(self, new_height: float):
        self._height = new_height
        self._width = new_height
        
    def set_side(self, new_side_length: float):
        self.set_width(new_side_length)
    
    def __str__(self) -> str:
        return f"Square(side={self.width})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))