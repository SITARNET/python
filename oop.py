# class Point:
#     "Класс Point"
#     x = 1 # статический атрибут
#     y = 1

# print(Point.__doc__) описание класса
# print(Point.__name__) название класса
# print(dir(Point)) служебные переменные
# pt = Point() # экземпляр класса
# print(pt.__dict__) # локальные переменные не существуют
# Point.x = 100
# print(pt.x, pt.y)
# print(id(pt), id(Point), sep="\n") # разные ячейки памяти
# print(id(pt.x), id(Point.x), sep="\n") # одинаковые ячейки памяти
# pt.x = 5 # атрибуты (свойства)
# pt.y = 10
# print(pt.x, Point.x)
# print(pt.__dict__) # локальные переменные существуют

# getattr(obj, name, [default]) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет на наличие атрибута name в obj
# setattr(obj, name, value) - задаёт значение атрибута объекта (если атрибута не существует, то он создаётся)
# delattr(obj, name) - удаляет атрибут с именем name
# print(getattr(pt, "x")) # 5
# print(getattr(pt, "z")) # AttributeError
# print(getattr(pt, "z", False)) # False
# print(hasattr(pt, "y")) # True

# setattr(pt, "z", 7)
# print(pt.__dict__) # {'x': 5, 'y': 10, 'z': 7}
# delattr(pt, "z")
# print(pt.__dict__) # {'x': 5, 'y': 10}
# del pt.x
# print(pt.__dict__)# {'y': 10}

# print(isinstance(pt, Point)) # являеться ли экземпляр экземпляром класса # True

# class Point3D:
#     x = 5
#     y = 10
#     z = 15
#
#
# pt1 = Point3D()
# print(pt1.x, pt1.y, pt1.z, sep="\n")
# setattr(pt1, "x", 10)
# setattr(pt1, "y", 20)
# setattr(pt1, "z", 30)
# print(pt1.__dict__)
# pt2 = Point3D()
# print(pt2.x, pt2.y, pt2.z, sep="\n")
# setattr(pt2, "x", 40)
# setattr(pt2, "y", 45)
# setattr(pt2, "z", 50)
# print(pt2.__dict__)
# print(pt2.x, pt2.y, pt2.z, sep="\n")
# delattr(pt2, "z")
# print(pt2.__dict__)


# class Point:
#     x = 1; y = 1
#     def setCoords(self): # self ссылаеться на экземпляр класса
#         print(self.__dict__)
#
# pt = Point()
# pt.x = 5
# pt.y = 10
# pt.setCoords()

class Point:
    def __init__(self, x = 0, y = 0): # конструктор
        self.x = x
        self.y = y

    def __del__(self): # деструктор удаляет экземпляры класса, если на него ничего не ссылаеться
        print("Удаление экземпляра: " + self.__str__())

    x = 1; y = 1
    def setCoords(self, x, y): # создаём через self локальные переменные для конкретного экземпояра класс
        self.x = x
        self.y = y

pt = Point()
# pt1 = Point(5)
# pt2 = Point(5, 10)
# # pt.setCoords(5, 10) # => Point.setCoords(pt, 5, 10)
# # print(pt.__dict__)
# print(pt.__dict__, pt1.__dict__, pt2.__dict__, sep='\n')
# pt = 0