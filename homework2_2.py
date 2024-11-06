# Базовый класс Figure
class Figure:
    unit = "cm"  # единица измерения

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе.")

    def info(self):
        raise NotImplementedError("Метод info должен быть реализован в подклассе.")

# Класс Square, наследуемый от Figure
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # приватный атрибут для длины стороны

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}²")

# Класс Rectangle, наследуемый от Figure
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # приватный атрибут для длины
        self.__width = width    # приватный атрибут для ширины

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}²")

# Создание списка фигур и вывод информации
if __name__ == "__main__":
    # Создаем объекты квадратов и прямоугольников
    figures = [
        Square(5),
        Square(7),
        Rectangle(5, 8),
        Rectangle(10, 15),
        Rectangle(3, 4)
    ]

    # Вывод информации о каждой фигуре
    for figure in figures:
        figure.info()
