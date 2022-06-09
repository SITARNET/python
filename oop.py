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

# 6, 7. OOP

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def isDigit(self):
#         if (isinstance(self.__x, int) or isinstance(self.__x, float)) and \
#                 (isinstance(self.__y, int) or isinstance(self.__y, float)):
#             return True
#         return False
#
#     def isInt(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width:int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def getWidth(self):
#         return self.__width
#
#     def setCoords(self, sp, ep): # меняет координаты линии, после того как она задана
#         if sp.isDigit() and ep.isDigit(): # проверка на int, float
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
# # class Line(Prop): # наследует от Prop
# #     def drawline(self):
# #         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
# #
# #     def __setOneCoord(self, sp):
# #         if sp.isInt():
# #             self._sp = sp
# #         else:
# #             print("Координата должна быть целочисленной")
# #
# #     def __setTwoCoords(self, sp, ep):
# #         if sp.isInt() and ep.isInt():
# #             # self._sp = sp
# #             # self._ep = ep
# #             Prop.setCoords(self, sp, ep)
# #         else:
# #             print("Координаты должны быть целочисленными")
# #
# #     def setCoords(self, sp: Point, ep: Point = None): # если один аргумент
# #         if ep is None:
# #             # if sp.isInt():
# #             #     self._sp = sp
# #             # else:
# #             #     print("Координата должна быть целочисленной")
# #             self.__setOneCoord(sp)
# #         else:
# #             # if sp.isInt() and ep.isInt():
# #             #     # self._sp = sp
# #             #     # self._ep = ep
# #             #     Prop.setCoords(self, sp, ep)
# #             # else:
# #             #     print("Координаты должны быть целочисленными")
# #             self.__setTwoCoords(sp, ep)
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определён метож draw()")
#
# class Line(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование треугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
#
# # class Rect(Prop): # наследует от Prop
# #     def drawRect(self):
# #         print(f"Рисование треугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")
#
# # print(isinstance(Point, object)) # True
#
# # l = Line(Point(1, 2), Point(10, 20))
# # l.drawline()
#
# # r = Rect(Point(30, 40), Point(70, 80))
# # r.drawRect()
# # print(l.__dict__)
# # l.drawline()
#
# # l.setCoords(Point(10, 20), Point(100, 200))
# # l.drawline()
# # l.setCoords(Point(-10, -20))
# # l.drawline()
#
# figs = []
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# 8. OOP

# class Point:
#     def __init__(self, x=0, y=0): # конструктор
#         self.__x = x
#         self.__y = y
#
#     def __str__(self): # строковое представление объекта
#         return f"({self.__x}, {self.__y})"
#
# class Styles:
#     def __init__(self):
#         print("Конструктор Styles")
#         super().__init__() # будет вызвано ровно один раз
#
# class Pos:
#     def __init__(self):
#         print("Конструктор Pos")
#         super().__init__() # будет вызвано ровно один раз
#
# class Line(Pos, Styles):
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# l = Line( Point(10, 10), Point(100, 100), "green", 5)
# l.draw()
# print(Line.__mro__) # список наследования

# # 9. OOP
#
# # class Clock
# # секунды отсчитываются от 00:00 часов ночи;
# # чмсло секунд не должно превышать значения: 24*60*60 = 86400
# # __DAY = 86400 - число секунд в дне
# # метод getFormatTime() - взврашает указанное время в формате: 01:32:02
# # s = self.__secs % 60 - секунды
# # m = (self.__secs // 60) % 60 - минуты
# # h = (self.__secs // 3600) % 24 - часы
#
# class Clock:
#     __DAY = 86400
#     def __init__(self, secs:int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY # не будет привышать 86400
#
#     def getFormatTime(self):
#         s = self.__secs % 60
#         m = (self.__secs // 60) % 60
#         h = (self.__secs // 3600) % 24
#         return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"
#
#     @staticmethod
#     def __getForm(x):
#         return str(x) if x > 9 else "0"+str(x)
#
#     def getSeconds(self):
#         return self.__secs
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Первый операнд должен быть типом Clock")
#
#         return Clock(self.__secs + other.getSeconds())
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Первый операнд должен быть типом Clock")
#
#         self.__secs += other.getSeconds()
#         return self
#
#     def __eq__(self, other):
#         # if self.__secs == other.getSeconds():
#         #     return True
#         # return False
#         return self.__secs == other.getSeconds()
#
#     def __nq__(self, other):
#         return not self.__eq__(other)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.__secs // 3600) % 24
#         if item == "min":
#             return (self.__secs // 60) % 60
#         if item == "sec":
#             return self.__secs % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.__secs % 60
#         m = (self.__secs // 60) % 60
#         h = (self.__secs // 3600) % 24
#
#         if key == "hour":
#             self.__secs = s + 60 * m + value * 3600
#         elif key == "min":
#             self.__secs = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.__secs = value + 60 * m + h * 3600
#
# c1 = Clock(100) # экземпляр класса
# c2 = Clock(100)
# c3 = Clock(300)
# # c3 = c1 + c2 # TypeError: unsupported operand type(s) for +: 'Clock' and 'Clock'
# # c3 = c1 + c2
# # print(c3.getFormatTime())
# # c3 = c1 +c2 -> __add__(self, other) -> c3 = c1.__add__(c2)
# # c1 += c2 -> __iadd(self, other) -> c1.__iadd__(c2)
# # c1 += c2 + c3
# # print(c1.getFormatTime())
#
# # x+y -> __add__(self, other)          x+=y -> __iadd__(self, other)
# # x-y -> __sub__(self, other)          x-=y -> __isub__(self, other)
# # x*y -> __mul__(self, other)          x*=y -> __imul__(self, other)
# # x/y -> __truediv__(self, other)      x/=y -> __itruediv__(self, other)
# # x//y -> __floordiv__(self, other)    x//=y -> __ifloordiv__(self, other)
# # x%y -> __mod__(self, other)          x%=y -> __imod__(self, other)
#
# if c1 == c2:
#     print("Времена равны")
#
# if c1 != c3:
#     print("Времена не равны")
#
# # x == y -> __eq__(self, other)
# # x != y -> __nq__(self, other)
# # x < y -> __lt__(self, other)
# # x <= y -> __le__(self, other)
# # x > y -> __gt__(self, other)
# # x >= y -> __ge__(self, other)
#
# # __getitem(self, item)
# # __setitem(self, key, value) - доступ к объектам по ключу
#
# c1["hour"] = 10 # __setItem(self, key, item) -> 10 1 40
# print(c1["hour"], c1["min"], c1["sec"]) # __getItem__(self, item)

# 10. OOP

# class CoordError(Exception): # своё исключение
#     pass
#
# class ImageXIterator:
#     def __init__(self, img, y: int):
#         self.__limit = img.width
#         self.__y = y
#         self.__img = img
#         self.__x = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__x >= self.__limit:
#             raise StopIteration
#
#         self.__x += 1
#         return self.__img[self.__x-1, self.__y]
#
# class ImageYIterator:
#     def __init__(self, img):
#         self.__limit = img.height
#         self.__img = img
#         self.__y = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__y >= self.__limit:
#             raise StopIteration
#
#         self.__y += 1
#         return ImageXIterator(self.__img, self.__y - 1)
#
# class Image:
#     def __init__(self, width, height, background="_"):
#         self.__background = background
#         self.__pixels = {}
#         self.__width = width
#         self.__height = height
#         self.__colors = {self.__background}
#
#     @property # будет возвращать ширину
#     def width(self):
#         return self.__width
#
#     @width.setter # будет устанавливать ширину
#     def width(self, width):
#         self.__width = width
#
#     @property  # будет возвращать высоту
#     def height(self):
#         return self.__height
#
#     @height.setter  # будет устанавливать высоту
#     def height(self, height):
#         self.__height = height
#
#     def __checkCoord(self, coord):
#         if not isinstance(coord, tuple) or len(coord) != 2:
#             raise CoordError("Координаты точки должны быть двухмерным кортежем")
#
#         if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
#             raise CoordError("Значения координат выходят за пределы изображения")
#
#     def __setitem__(self, coord, color):
#         self.__checkCoord(coord)
#
#         if color == self.__background:
#             self.__pixels.pop(coord, None) # удаляем пиксел с соответствующими координатами из славаря,
#             # если пиксела с такой координатой нету -> None
#         else:
#             self.__pixels[coord] = color
#             self.__colors.add(color) # в политру colors добовляем цвет
#
#     def __getitem__(self, coord):
#         self.__checkCoord(coord)
#         return self.__pixels.get(coord, self.__background)
#
#     def __iter__(self):
#         return ImageYIterator(self)
#
# # class MyIter:
# #     def __init__(self, limit):
# #         self.__num = 0
# #         self.__limit = limit
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         if self.__num >= self.__limit:
# #             raise StopIteration
# #         self.__num += 1
# #         return self.__num
# #
# # it = MyIter(10)
# # for i in it:
# #     print(i)
#
# img = Image(20, 4)
# # img[1, 1] = "*"
# # color = img[5, 5]
# # print(img.width, img.height)
#
# img[1, 1] = "*"; img[2, 1] = "*"; img[3, 1] = "*"
# # for y in range(img.height):
# #     for x in range(img.width):
# #         print(img[x, y], sep=" ", end="")
# #     print()
#
# for row in img: # чтобы объект img был итерируемым
#     for pixel in row:
#         print(pixel, sep=" ", end="")
#     print()
#
# # __iter__(self) -> it = MyIter(10) объект берётся для итерации
# # __next__(self) -> for i in it когда в цикле for берём следующее значение

# 11. OOP

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs): # делает объект, который можно вызывать как функцию - функтор
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
# c1 = Counter()
# c1() # 1
# c1() # 2
# c2 = Counter() # будкт работать независимо
# c2() # 1
# c2() # 2


# class StripChars:
#     def __init__(self, chars): # символы которые нужно удвлять
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)

# def StripChars(chars): # классический пример замыкания
#     def stringStrip(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#     return stringStrip
#
# s1 = StripChars("?:!.; ") # будет ссылаться на функцию stringStrip()
# print(s1(" Hello World! ")) # "Hello World"
# s2 = StripChars("?:!.; ")
# print(s1(" Hello? "))
# print(id(s1), id(s2), sep="\n") # разные объекты

# Менеджеры контекста

# fp = None
# try:
#     fp = open("my_file.txt")
#     for t in fp:
#         print(t)
# except Exception as e:
#     print(e)
# finally:
#     if fp is not None:
#         fp.close()


# try:
#     with open("my_file.txt") as fp: # менеджер контекста, автоматически закрывает поток
#         for t in fp:
#             print(t)
# except Exception as e:
#     print(e)

# Собственный менеджер контекста
# __enter__()    __exit__()
# width<менеджер контекста>as<переменная>:
#     список конструкций языка Python

# class DefenerVector:
#     def __init__(self, v):
#         self.__v = v
#
#     def __enter__(self):
#         self.__temp = self.__v[:] # делаем копию вектора v, dv будет ссылаться на __temp
#         return self.__temp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None: # если небыло никаких исключений
#             self.__v[:] = self.__temp # в v1 запишем результат сложения
#         return False
#
# v1 = [1, 2, 3] # v1 += v2, если возникнут ошибки, вектор v1 должен остаться как и был
# v2 = [1, 2]
# try:
#     with DefenerVector(v1) as dv:
#         for i in range(len(dv)):
#             dv[i] += v2[i]
# except Exception as e:
#     print(e)
#
# print(v1) # v2 = [1, 2, 3] -> [2, 4, 6], v2 = [1, 2] -> list index of range [1, 2, 3]

# Вложенность

# try:
#     with open("my_file.txt") as fin:
#         with open("out.txt", "w") as fout:
#             for line in fin:
#                 fout.write(line)
# except Exception as e:
#     print(e)

# 13. OOP

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
# # Если нам нужен метод, который бы "работал" с атрибутами экземпляров классов, то это однозначно обычный метод с первым
# # парвметром self, который указывает на текущий объект.
#     def setCoords(self, x, y):
#         if Vector.validate(x) and Vector.validate(y):
#             self.x = x
#             self.y = y
#
# # Если нужен метод, который можно вызывать непосредственно из класса (или экземпляра) и,  который бы имел доступ к
# # свойствам и методам этого класса, то его следует объявить как метод класса через декоратор @classmethod.
#     @classmethod
#     def validate(cls, arg):
#         if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
#             return True
#         return False
#
# # Если нужен метод, который можно вызывать непосредственно мз класса, но доступ к его атрибутам не предпологается, то
# # достаточно его объявить как статический, через докоратор @staticmrthod.
#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y

# 14. OOP

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def getPerimetr(self):
#         return 2*(self.w + self.h)
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def getPerimetr(self):
#         return 4*self.a
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def getPerimetr(self):
#         return self.a + self.b + self.c
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# geom = [r1, r2, s1, s2, t1, t2] # коллекция
#
# for g in geom: # перебираем коллекцию
#     print(g.getPerimetr()) # 6 14 40 80 6 15


# 15. OOP

# Пример реализации "Моносостояния"

class ThreadData:
    __common_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = ThreadData.__common_attrs

th1 = ThreadData()
th2 = ThreadData()

th2.id = 3
th1.attr_new = 'new attr'
print(th2.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 3, 'attr_new': 'new attr'}
print(th1.__dict__) # {'name': 'thread_1', 'data': {}, 'id': 3, 'attr_new': 'new attr'}
print(id(th1.__dict__)) # 139797797284224
print(id(th2.__dict__)) # 139797797284224