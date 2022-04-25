# def make_upper_case(s):
#     # Code here
#     s = s.upper()
#     return s
#
# #make_upper_case("eee")
#
# def string_to_array(s):
#     b = s.split(" ")
#     return b
#
# #a = string_to_array("I am Nikolay")
# #print(a)
#
# def invert(lst):
#     b = []
#     for i in lst:
#         if i > 0:
#             b.append(-i)
#         else:
#             b.append(-i)
#     return b

#c = invert([-1, 6, 5, -3, 4])
#print(c)


import statistics

def better_than_average(class_points, your_points):
    middle = int(statistics.mean(class_points))
    print(middle)
    if middle < your_points:
        return True
    else:
        return False

b = better_than_average([3, 7], 2)
print(b)