from abc import *

class Polygon(metaclass = ABCMeta):
    @abstractclassmethod
    def area(self):
        print('면적 구하기 메소드 구현')
    
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(2.4, 4.3)
print('사각형 면적: %.2f' % rect.area())