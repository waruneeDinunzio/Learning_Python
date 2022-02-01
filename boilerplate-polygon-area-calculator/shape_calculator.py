class Rectangle:
  def __init__(self, width ,height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (self.width*2)+(self.height * 2)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    string = (("*"* self.width) + "\n") * self.height
    return string

# """ Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
# """ 
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"