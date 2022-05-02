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


# import statistics
#
# def better_than_average(class_points, your_points):
#     middle = int(statistics.mean(class_points))
#     print(middle)
#     if middle < your_points:
#         return True
#     else:
#         return False
#
# b = better_than_average([3, 7], 2)
# print(b)

# def rental_car_cost(d):
#     if d >= 7:
#         price = (d * 40) - 50
#     elif 3 <= d < 7:
#         price = (d * 40) - 20
#     else:
#         price = d * 40
#     return price
#
# print(rental_car_cost(6))

# def positive_sum(arr):
#     s = 0
#     for i in arr:
#         if i > 0:
#             s += i
#     return s
#
#
# a = positive_sum([])
# print(a)

# def no_space(x):
#     #your code here
#     x = ''.join(x.split())
#     return x
#
#
# a = no_space('jfBm  gk lf8hg  88lbe8 ')
# print(a)


# def solution(string):
#     reversed_string = string[::-1]
#     return reversed_string
#
#
# print(solution("World"))


# def friend(x):
#     #Code
#     new_friends = []
#     for i in x:
#         if len(i) == 4:
#             new_friends.append(i)
#     return new_friends
#
#
# print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))


# def printer_error(s):
#     # your code
#     colors = "abcdefghijklm"
#     len_s = len(s)
#     count_colors_out = 0
#     for i in s:
#         if i not in colors:
#             count_colors_out += 1
#
#     return "{}/{}".format(count_colors_out, len_s)
#
# s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# print(printer_error(s))


# def binary_array_to_number(arr):
#     # your code
#     string_str = ""
#     for i in arr:
#         i = str(i)
#         string_str += i
#
#     return int(string_str, 2)
#
#
# print(binary_array_to_number([0, 1, 1, 0]))


# def abbrev_name(name):
#     name_c = name.split()
#     first = name_c[0][0].capitalize()
#     second = name_c[1][0].capitalize()
#     return ("{}.{}".format(first, second))
#
# print(abbrev_name("patrick feenan"))


def maps(a):
    new_list = []
    for i in a:
        i *= 2
        new_list.append(i)
    return new_list


print(maps([2, 4, 8]))