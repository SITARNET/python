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


# def calculate_years(principal, interest, tax, desired):
#     years = 0
#     while principal < desired:
#         years = years + 1
#         total_interest = principal * interest
#         interest_tax = total_interest * tax
#         principal = principal + (total_interest - interest_tax)
#     return years
#
# print(calculate_years(1000, 0.05, 0.18, 1100))


# def accum(s):
#     list_new = []
#     s = list(s)
#     index = 0
#     while index < len(s):
#         for i in s:
#             index += 1
#             list_new.append((i * index).capitalize())
#         list_new = '-'.join(list_new)
#         return list_new
#
# # return '-'.join((c * i).title() for i, c in enumerate(s, 1))
#
#
# print(accum("aBcd"))

# def sum_mix(arr):
#     new_arr = []
#     for i in arr:
#         if type(i) == str:
#             i = int(i)
#             new_arr.append(i)
#         else:
#             new_arr.append(i)
#     sum_arr = sum(new_arr)
#     return sum_arr
#
# # return sum(map(int, arr))
#
# print(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']))


# def century(year):
#     if year % 100 > 0:
#         cen = int(year / 100 + 1)
#         return cen
#     else:
#         cen = int(year / 100)
#         return cen
#
#
# print(century(2022))


# def century(year):
#     return (year + 99) // 100


# def solution(string, ending):
#     return string.endswith(ending)
#
# print(solution('abcde', 'cde'))


# def greet():
#     return "hello world!"
#
# print(greet())


# def to_jaden_case(string):
#     lt = string.split()
#     a = []
#     for i in lt:
#         i = i.capitalize()
#         a.append(i)
#     return ' '.join(a)
#
# # return string.capwords(NonJadenStrings)
#
# string = "How can mirrors be real if our eyes aren't real"
# print(to_jaden_case(string))


# def get_grade(s1, s2, s3):
#     cen = (s1 + s2 + s3) / 3
#     if 90 <= cen <= 100:
#         return "A"
#     elif 80 <= cen < 90:
#         return "B"
#     elif 70 <= cen < 80:
#         return "C"
#     elif 60 <= cen < 70:
#         return "D"
#     if 0 <= cen < 60:
#         return "F"
#
#
# print(get_grade(72, 70, 75))


# def simple_multiplication(number):
#     if number % 2 == 0:
#         number *= 8
#         return number
#     else:
#         number *= 9
#         return number
#
# # return number * (8 if number % 2 == 0 else 9)
#
# print(simple_multiplication(4))


# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 > 0:
#             return i
#
#
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))


# def digitize(n):
#     n = str(n)
#     arr = []
#     for i in n:
#         arr.append(int(i))
#     return arr[::-1]
#
# # return map(int, str(n)[::-1])
#
# print(digitize(23582357))


# def remove_char(s):
#     # s = list(s)
#     # del s[0], s[-1]
#     # s = ''.join(s)
#     # return s
#
#     return s[1 : -1]
#
# print(remove_char('eloquent'))


# def tower_builder(n_floors):
#     # tower = []
#     # floor = ''
#     # for f in range(n_floors):
#     #     stars = '*' * (f * 2 + 1)
#     #     spaces = ' ' * (n_floors - f - 1)
#     #     floor = spaces + stars + spaces
#     #     tower.append(floor)
#     # return tower
#
#     return [("*" * (i * 2 - 1)).center(n_floors * 2 - 1) for i in range(1, n_floors + 1)]
#
# print(tower_builder(6))


# def is_divide_by(number, a, b):
#     if number % a == 0 and number % b == 0:
#         return True
#     else:
#         return False
#
# print(is_divide_by(15, -5, 3))


# def array_diff(a, b):
#     if len(b) == 0:
#         return a
#     for i in b:
#         if i in a:
#             for n in range(a.count(i)):
#                 a.remove(i)
#     return a
#
#
# print(array_diff([1, 2, 2, 2, 3], [1, 3]))


# def reverse_words(text):
#     a = text.split(' ')
#     b = []
#     for i in a:
#         i = i[::-1]
#         b.append(i)
#     c = " ".join(b)
#     return c
#
#     # return ' '.join(s[::-1] for s in str.split(' '))
#
# print(reverse_words('double spaced words'))


# def double_integer(i):
#     return i + i
#
#     # return i * 2
#
# print(double_integer(-336))


# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
#
#     # return eval(f'{value1}{operator}{value2}')
#
# print(basic_op('+', 4, 7))


# def find_average(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         index = 0
#         for i in numbers:
#             index += i
#         print(index)
#         t = index / len(numbers)
#         return t
#
#     # return sum(array) / len(array) if array else 0
#
# print(find_average([1, 2, 6]))


# def smash(words):
#     return ' '.join(words)
#
#
# print(smash(["hello", "amazing", "world"]))


# def descending_order(num):
#     ls = list(str(num))
#     lsn = []
#     for i in ls:
#         lsn.append(i)
#     a = sorted(lsn)[::-1]
#     a = int(''.join(a))
#     return a
#
#     # return int("".join(sorted(str(num), reverse=True)))
#
# print(descending_order(145263))


# def open_or_senior(data):
#     user_list = []
#     for user in data:
#         if user[0] >= 55 and user[1] >= 7:
#                 user_list.append("Senior")
#         else:
#             user_list.append("Open")
#     return user_list
#
#     # return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
#
# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))


# def lovefunc( flower1, flower2 ):
#     if flower1 % 2 == 0 and flower2 % 2 == 0 or flower1 % 2 != 0 and flower2 % 2 != 0:
#         return False
#     else:
#         return True
#
#     # return (flower1 + flower2) % 2 != 0
#
# print(lovefunc(1, 4))


# def find_smallest_int(arr):
#     a = min(arr)
#     return a
#
#     # return min(arr)
#
# print(find_smallest_int([34, -345, -1, 100]))


# def find_needle(haystack):
#     for i in haystack:
#         i = str(i)
#         if i == "needle":
#             index = haystack.index(i) + 1
#             a = "found the needle at position {}".format(index)
#             return a
#
#     # return 'found the needle at position {}'.format(haystack.index('needle'))
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))


# def sort_array(source_array):
#     odd = sorted(list(filter(lambda x: x % 2, source_array)))
#     l, c = [], 0
#     for i in source_array:
#         if i in odd:
#             l.append(odd[c])
#             c += 1
#         else:
#             l.append(i)
#     return l
#
#
# print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


# def area_or_perimeter(l , w):
#     if l == w:
#         sq = l * w
#         return sq
#     else:
#         sq = 2 * l + 2 * w
#         return sq
#
#
# print(area_or_perimeter(6, 3))


# def get_count(sentence):
#     vowels = "aeiou"
#     count = 0
#     for i in sentence:
#         for a in vowels:
#             if a == i:
#                 count += 1
#     return count
#
#     # return sum(c in 'aeiou' for c in s)
#
# print(get_count("abracadabra"))


# def find_nb(m):
#     total = 0
#     n = 0
#     while (total < m):
#         n = n + 1
#         total = total + n ** 3
#     return n if total == m else -1
#
#
# print(find_nb(135440716410000))


# def min_max(lst):
#     app = []
#     app.append(min(lst))
#     app.append(max(lst))
#     return app
#
#     # return [min(lst), max(lst)]
#
# print(min_max([1, 2, 3, 4, 5]))


# def get_middle(s):
#     ln = len(s)
#     if ln % 2 != 0:
#         return s[int(ln / 2)]
#     else:
#         return s[int(ln / 2 - 1)] + s[int(ln / 2)]
#
#
# print(get_middle("testing"))


# def double_char(s):
#     s = list(s)
#     arr = []
#     for i in s:
#         i += i
#         arr.append(i)
#     return ''.join(arr)
#
#     # return ''.join(c * 2 for c in s)
#
# print(double_char("Hello World"))


# def is_pangram(s):
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     for st in letters:
#         if st not in s.lower():
#             return False
#     return True
#
#
# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))



# def is_valid_walk(walk):
#     time = 10
#     step = len(walk)
#     if step != time:
#         return False
#     else:
#         count_n, count_s, count_w, count_e = 0, 0, 0, 0
#         for i in walk:
#             if i == 'n':
#                 count_n += 1
#             elif i == 's':
#                 count_s += 1
#             elif i == 'w':
#                 count_w += 1
#             elif i == 'e':
#                 count_e += 1
#         if count_n == count_s and count_w == count_e:
#             return True
#         else:
#             return False
#
#     # return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
#
# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))


# def count_by(x, n):
#     # arr = []
#     # for i in range(1, n + 1):
#     #     i *= x
#     #     arr.append(i)
#     # return arr
#     return [i * x for i in range(1, n + 1)]
#
# print(count_by(3, 10))


# def count_positives_sum_negatives(arr):
#     # arr_new = []
#     # count_plus = 0
#     # a = 0
#     # if arr != []:
#     #     for i in arr:
#     #         if i > 0:
#     #             count_plus += 1
#     #         else:
#     #             a += i
#     #     arr_new.append(count_plus)
#     #     arr_new.append(a)
#     #     return arr_new
#     # else:
#     #     return arr_new
#
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


# def decrypt(s, n):
#     if not s: return s
#     o, l = len(s) // 2, list(s)
#     for _ in range(n):
#         l[1::2], l[::2] = l[:o], l[o:]
#     return ''.join(l)
#
#
# def encrypt(s, n):
#     if not s: return s
#     for _ in range(n):
#         s = s[1::2] + s[::2]
#     return s
#
#
# print(decrypt("012345", 2))
# print(encrypt("135024", 2))


# # def find_even_index(array):
# #     for index in range(len(array)):
# #         if sum(array[:index]) == sum(array[index + 1:]):
# #             return index
# #     return -1
#
#
# def find_even_index(lst):
#     left_sum = 0
#     right_sum = sum(lst)
#     for i, a in enumerate(lst):
#         right_sum -= a
#         if left_sum == right_sum:
#             return i
#         left_sum += a
#     return -1
#
#
# print(find_even_index([10, -80, 10, 10, 15, 35, 20]))


# def likes(names):
#     len_names = len(names)
#     if len_names == 0:
#         return 'no one likes this'
#     elif len_names == 1:
#         return '{} likes this'.format(names[0])
#     elif len_names == 2:
#         return '{} and {} like this'.format(names[0], names[1])
#     elif len_names == 3:
#         return '{}, {} and {} like this'.format(names[0], names[1], names[2])
#     else:
#         others = len_names - 2
#         return '{}, {} and {} others like this'.format(names[0], names[1], others)
#
#
# print(likes(['Max', 'John']))


def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)