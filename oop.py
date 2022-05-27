# 1. OOP

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

# 2. OOP

# class Point:
#     x = 1; y = 1
#     def setCoords(self): # self ссылаеться на экземпляр класса
#         print(self.__dict__)
#
# pt = Point()
# pt.x = 5
# pt.y = 10
# pt.setCoords()

# class Point:
#     def __init__(self, x = 0, y = 0): # конструктор
#         self.x = x
#         self.y = y
#
#     def __del__(self): # деструктор удаляет экземпляры класса, если на него ничего не ссылаеться
#         print("Удаление экземпляра: " + self.__str__())
#
#     x = 1; y = 1
#     def setCoords(self, x, y): # создаём через self локальные переменные для конкретного экземпояра класс
#         self.x = x
#         self.y = y
#
# pt = Point()
# # pt1 = Point(5)
# # pt2 = Point(5, 10)
# # # pt.setCoords(5, 10) # => Point.setCoords(pt, 5, 10)
# # # print(pt.__dict__)
# # print(pt.__dict__, pt1.__dict__, pt2.__dict__, sep='\n')
# # pt = 0

# 3. OOP

# class Point:
#     WIDTH = 5
#
#     # __slots__ = ["__x", "__y"] # дабавляет разрешонные свойства
#
#     def __init__(self, x = 0, y = 0):
#         self.__x = x
#         self.__y = y
#
# # x - публичное свойство "public"
# # _x - можно обращаться только внутри класса и во всех его дочерних классах "protected"
# # __x - можно обращаться только внутри коасса "private"
#
#     def __checkValue(x): # делаем проверку через приватный метод
#         if isinstance(x, int) or isinstance(x, float):
#             return True
#         return False
#
#     def setCoords(self, x, y): # публичный метод
#         if Point.__checkValue(x) and Point.__checkValue(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def getCoords(self): # чтобы вернуть, увидеть результат
#         return self.__x, self.__y
#
#     def __getattribute__(self, item): # перегрузка метода
#         if item == "_Point__x":
#             return "Частная переменная"
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == "WIDTH": # если происходит изменение свойства WIDTH
#             raise AttributeError
#         else:
#             self.__dict__[key] = value # для других свойств можем менять
#
#     def __getattr__(self, item): # вызываеться если несуществует свойство
#         print("__getattr__" + item)
#
#     def __delattr__(self, item): # вызываеться если удалено свойство
#         print("__delattr__" + item)
#
#
# pt = Point(1, 2)
# # print(pt.getCoords())
# # pt.setCoords("10", 20)
# # print(pt.getCoords())
# # можно обратиться к приватным методам и атрибутам  _Имя класса__имя переменной или _Имя класса__имя метода
# # print(pt._Point__x)
# # Point._Point__checkValue(4)
# # но так работать нельзя
#
# # __setattr__(self, key, value) - автоматически вызываеться при изменении свойства key класса
# # __getattribute__(self, item) - автоматически вызываеться при получении свойства класса с именем item
# # __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# # __delattr__(self, item) - автоматически вызываеться при удалении свойства item (не выжно: существует оно или нет)
#
# # pt.WIDTH = 5
#
# pt.zzz # __getattr__zzz
# pt.z = 1
# del pt.z # __delattr__z

# 4. OOP

# class NoDataDescr:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, value): # только один метод get - считывание
#         return "NoDataDescr __get__"
#
#
# class CoordValue:
#     def __set_name__(self, owner, name):
#         print(name)
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         # return self.__value
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         # self.__value = value
#         instance.__dict__[self.__name] = value
#
#     # def __delete__(self, obj):
#     #     del self.__value
#
# class Point:
#     noData = NoDataDescr()
#     coordX = CoordValue()
#     coordY = CoordValue()
#
#     def __init__(self, x=0, y=0):
#         self.coordX = x
#         self.coordY = y
#
#     # def __chechVaue(x):
#     #     if isinstance(x, int) or isinstance(x, float):
#     #         return True
#     #     return False
#     #
#     # # def __getCoordX(self):
#     # #     # print("Вызов __getCoordX")
#     # #     return self.__x
#     #
#     # @property # декоратор
#     # def coordX(self):
#     #     return self.__x
#     #
#     # # def __setCoordX(self, x):
#     # #     if Point.__chechVaue(x):
#     # #         # print("Вызов __setCoordX")
#     # #         self.__x = x
#     # #     else:
#     # #         raise ValueError("Неверный формат данных")
#     #
#     # @coordX.setter
#     # def coordX(self, x):
#     #     if Point.__chechVaue(x):
#     #         self.__x = x
#     #     else:
#     #         raise ValueError("Неверный формат данных")
#     #
#     # # def __delCoordX(self):
#     # #     # print("Удаление свойства")
#     # #     del self.__x
#     #
#     # @coordX.deleter
#     # def coordX(self):
#     #     del self.__x
#     #
#     # # coordX = property(__getCoordX, __setCoordX, __delCoordX)
#
#
# pt = Point(1, 2)
# print(pt.coordX, pt.coordY)
# # pt.coordX = 100 # запись значения
# # x = pt.coordX # чтение значения
# # print(x)
# # del pt.coordX # удаляет свойство х
# # pt.coordX = 7
# # pt.coordX
#
# pt2 = Point(5, 10)
# print(pt2.coordX, pt2.coordY)
#
# pt.noData = "hello"

# 5. OOP

# class Point:
#     __count = 0
#     __instance = None
#
#     def __new__(cls, *args, **kwargs): # singleton - создание одного экземпляра класса
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super(Point, cls).__new__(cls)
#         else:
#             print("Экземпляр класса Point уже создан!")
#
#     def __init__(self, x=0, y=0):
#         Point.__count += 1
#         self.coordX = x
#         self.coordY = y
#
#     @staticmethod
#     def getCount(): # статический метод, self не надо
#         return Point.__count
#
# pt = Point()
# pt1 = Point()
# pt2 = Point()
# # # Point.getCount(1) # 3
# # print(pt.getCount(), Point.getCount()) # 3 3
# print(id(pt), id(pt1), id(pt2), sep="\n")

# 6. OOP

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width:int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width

class Line(Prop): # наследует от Prop
    def drawline(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")

class Rect(Prop): # наследует от Prop
    def drawRect(self):
        print(f"Рисование треугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")

# print(isinstance(Point, object)) # True

l = Line(Point(1, 2), Point(10, 20))
l.drawline()

r = Rect(Point(30, 40), Point(70, 80))
r.drawRect()
print(l.__dict__)
l.drawline()