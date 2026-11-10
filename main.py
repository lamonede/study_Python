# import copy

# x = [1,2,3]
# y = copy.deepcopy(x)

# def add(a,b):
#     """add num"""
#     return a+b



# print(x == y)
# print(x is y)
# print(x[0] == y[0])
# print(x[0] is y[0])

# 2026.09.21

# import copy

# a = [10]
# b = a
# # b = copy.deepcopy(a)

# b.append(1)

# print(a, b)

# def add_student(name, students=[]):
#     students.append(name)
#     return students

# print(add_student("a"))
# print(add_student("b"))
# print(add_student("c"))

# def func(**lemon):
#     return lemon

# a = {"var": 2}

# print((func(a)))
# print(type(a))

# numbers = [10, 20, 30]

# def add(*nums):
#     a = 0
#     for i in nums:
#         a = a + i
#     return a

# print(add(*numbers))

# def change(x):
#     print(id(x))
#     x = [10, 20, 30]
#     print(id(x))

# a = [1, 2, 3]
# print(id(a))
# a = [2, 3, 4]
# print(id(a))
# # change(a)
# # print(a)

# x = 124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384
# print(id(x))
# def f():
#     x = 124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384124910394920349234982049829384
#     print(id(x))
#     print(x)

# f()
# print(id(f))

# x = 10

# def f():
#     x = 20
#     print(id(x))
#     print(x)

# f()
# print(id(f))

# x = [1,2,3]

# def f():
#     x = [1,2,3]
#     print(id(x))
#     print(x)

# f()
# print(id(f))

# students = ["a", "b", "c"]
# def add_students(name, students=[]):
#     students.append(name)
#     print(id(students))
#     return students

# print(add_students(students))
# print(add_students("e"))

# x = 10
# print(id(x))

# def f():
#     # global x
#     print(id(x))
#     x = 20

# f()
# x     x is None   not x
# None  T           T
# 0     F           T
# ""    T           T
# []    T           T       [] is not none

# x = ["a"]
# if x:
#     print("X is True")

# def add_students(name, students=None):
#     if not students:
#         students = []
#     students.append(name)
#     print(id(students))
#     return students

# print(add_students("신연호", x))
# print(x)

# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))
# y = [10, 20, 30]
# print(y, id(y))
# y[1] = 50
# print(y, id(y))

# x = [10, 20, 30]
# print(id(x[0]), id(x[1]), id(x[2]))

# x = 10
# y = x
# y = 5

# print(x, y)   
# print(id(x), id(y))

# import copy

# x = [[10, 20], 30]
# y = copy.copy(x)

# print(x[0], y[0])
# print(id(x[0]), id(y[0]))
# import copy

# a = [[1,3,5,7]]
# b = copy.copy(*a)
# print(*b)

# t = (10, [20, 30])
# print(id(t))
# print(id(t[1]))

# t[1][0] = 99
# print(t)
# print(id(t))
# print(id(t[1]))

# def add_students(name, students=None):
#     print(id(students))
#     if not students:
#         students = []
#         print(id(students))
#     students.append(name)
#     return students
# a = []
# print(id(a))
# print(add_students("박지호", []))

# students = [1,2,3]
# print(id(students))

# def add_students(name, students=None):
#     print(id(students))
#     students = [1,2,3,4]
#     print(id(students))

#     return students

# print(add_students("a", students))
# print(students)

# print(locals())
# print(10 and 20)

# True and test() | False or test()

# def a():
#     print("A")
#     return ['a']

# def b():
#     print("B")
#     return ['b']

# result = a() and b()
# print(result)

# mem = [] and "앞에는 truthy"
# print(mem)

# students = []

# def get_students():
#     return students

# if get_students():
#     print("A")
# else:
#     print("B")

# def lemon():
#     print("1")
#     return True

# def lemonade():
#     print("2")
#     return True

# def citrus():
#     print("3")
#     return False

# print(lemon() and not lemonade() or citrus())

# a = True
# b = False

# print(not a == b not (a == b) a == not b)

# a = complex(2, 7)
# print(a)
# print(a*a)

# a = [1, 3, 5, 7, 9]
# a.append(10)
# print(a)

# b = ['a', 1, 1.2, True]
# b.pop(3)
# print(b)

# c = ("lemonade",)
# print(c)

# d = (20, "shin", False)
# d.append()
# print(d)

# tmp1_text = b"lemonade"

# print(tmp1_text)

# s = {1, 2, 2, 3, 3, 3}
# print(s)

# s = {}
# print(type(s))
# s_1 = set()
# print(type(s_1))

# lemon_dict = {'lemon': 20, 'sugar': 25, 'water': 10}
# print(lemon_dict)

# print(1.1 + 0.1)

# x = [1, 2]
# x += [3]
# print(x)

# print(115792089237316195423570985008687907853269984665640564039457584007913129639936//100000000)

for r in range(1, 10, 2):
    r[i] =  i
print(r[0])
