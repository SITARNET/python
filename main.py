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


# def maps(a):
#     new_list = []
#     for i in a:
#         i *= 2
#         new_list.append(i)
#     return new_list
#
#
# print(maps([2, 4, 8]))


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     auto_dist = fuel_left * mpg
#     if auto_dist >= distance_to_pump:
#         return True
#     else:
#         return False
#
# print(zero_fuel(12, 24, 4))


# def count_sheep(n):
#     a = "sheep..."
#     sheeps = ""
#     for i in range(1, n+1):
#         sheep = str(i) + " " + a
#         sheeps += sheep
#     return sheeps
#
#
# print(count_sheep(5))


# def dna_to_rna(dna):
#     dna_new = dna.replace("T", "U")
#     return dna_new
#
# print(dna_to_rna("GCA"))


# def paperwork(n, m):
#     if n < 0 or m < 0:
#         return 0
#     else:
#         return n * m
#
#
# print(paperwork(5, 6))


# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)
#
#
# print(maximum([-52, 56, 30, 29, -54, 0, -110]))
# print(minimum([-52, 56, 30, 29, -54, 0, -110]))


# def check(seq, elem):
#     if elem in seq:
#         return True
#     else:
#         return False
#
# # return elem in seq
#
#
# print(check(["when's", "the", "next", "Katathon?", 9, 7], "the"))


# def string_to_number(s):
#     n = int(s)
#     return n
#
#
# print(string_to_number("543"))


# def DNA_strand(dna):
#         dnanew = ''
#         for d in dna:
#                 if d == 'A':
#                         dnanew += 'T'
#                 elif d == 'T':
#                         dnanew += 'A'
#                 elif d == 'G':
#                         dnanew += 'C'
#                 elif d == 'C':
#                         dnanew += 'G'
#         return dnanew

#         return dna.translate(str.maketrans("ATCG","TAGC"))
#
# print(DNA_strand("AAATTT"))


# import math
#
# def find_next_square(sq):
#     t = math.sqrt(sq)
#     if t.is_integer():
#         int_num = math.sqrt(sq) + 1
#         return int_num ** 2
#     else:
#         return -1
#
#
# print(find_next_square(121))


# def reverse_seq(n):
#     arr = []
#     for i in range(1, n+1):
#         arr.append(i)
#     return arr[::-1]
#
# print(reverse_seq(8))


# def summation(num):
#     sum = 0
#     for i in range(1, num+1):
#         sum += i
#     return sum
#
# # return sum(range(num + 1))
#
# print(summation(8))


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        years = years + 1
        total_interest = principal * interest
        interest_tax = total_interest * tax
        principal = principal + (total_interest - interest_tax)
    return years

print(calculate_years(1000, 0.05, 0.18, 1100))