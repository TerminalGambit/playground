# understanding better the use of __str__ and __repr__ methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y}, str method)'

    def __repr__(self):
        return f'Point({self.x}, {self.y}) repr method'

p = Point(1, 2)
print(str(p))
print(repr(p))
print(p) # __str__ is called by default
print(f'{p}') # __str__ is called by default
print(f'{p!r}') # __repr__ is called by default

# __str__ is used for the end user

# __repr__ is used for the developer