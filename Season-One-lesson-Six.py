# function_review functions_advanced
def my_sum(*args):
    print(args)
    # tup = (a, b, c, d, e)
    # return sum(args)



args_call = (1, 2, 3, 1000, 1)
# res = my_sum(1, 2, 3, 1000, 1)
res = my_sum(*args_call)


print(res)
#--------------------------------------------------------------
# functions_kwargs
def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    # kwargs['mode']
    mode = kwargs.get('mode', 'nothing')
    print(mode)


fun(1, 2, 3, 4, 5, state='nothing', val=1)
#--------------------------------------------------------------
# key_word_arrgs
import math


# def distance(x, y):
#     return math.sqrt(x**2 + y**2)


def distance(x, y, norm=2, mode=100):
    print("mode --> ", mode)
    a = x ** norm + y ** norm
    b = a ** (1/norm)
    return b


print(distance(12, 5, norm=1))
print(distance(3, 4, mode=1000000))
#------------------------------------------------------------------------
# reimplement_zip
def my_zip(*args):
    len_list = len(args[0])
    len_tuple = len(args)
    out = []
    for i in range(len_list):
        tmp = []
        for j in range(len_tuple):
            tmp.append(args[j][i])
        tmp = tuple(tmp)
        out.append(tmp)

    return out


x = [1, 2, 3, 4, 1, 2, 3]
y = [0, 9, 1, 1, 3, 3, 6]
z = [1, 3, 0, 2, 4, 6, 0]
res = my_zip(x, y, z, x, y, z)

print(res)
# [(1, 0), (2, 9), (3, 1), (4, 1)]
# my_zip(x, y, z)
# [(1, 0, 1), (2, 9, 3), (3, 1, 0), (4, 1, 2)]
#--------------------------------------------------------------------------------
# review
import math


def combination(n, m):
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    result = numerator / denominator
    return str(int(result)).center(6)


def pascal_row(n):
    row = []
    for i in range(n + 1):
        val = combination(n, i)
        row.append(val)
    return row


def pascal(rows):
    res = []
    for i in range(rows + 1):
        current_row = pascal_row(i)
        res.append(current_row)
    return res


res = pascal(15)

for r in res:
    row = ''.join(r)
    print(row.center(100))
    # print(*r, sep='\t')
#----------------------------------------------------------------------------
# generators generators
def fib(n):
    i = 0
    a, b = 1, 1
    yield 1
    yield 1
    while i < n:
        i += 1
        a, b = b, a + b
        yield b


gen = fib(10)
print(gen)
v1 = next(gen)
v2 = next(gen)
v3 = next(gen)
# v4 = next(gen)
# v5 = next(gen)

print(list(gen))
#
# for i in gen:
#     print(i)
#
# 1  1
# 2  1 1
# 3  1 1 1
# 4  1 1 1 1
# 5  1 1 1 1 1
# 6  1 1 1 1 1 1
# 7  1 1 1 1 1 1 1
# 8  1 1 1 1 1 1 1 1
# 9  1 1 1 1 1 1 1 1 1
#
# 1  1
# 2    1
# 3      1
# 4        1
# 5          1
# 6            1
# 7              1
# 8                1
# 9                  1
#-----------------------------------------------------------------------------
# why_generators

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'*' * 1    # 10*INT + 1*STR
'*' * 2    # 10*INT + 1*STR


i = 1
stop = 10
'*' * i   # 2*INT + 1*STR
i = i + 1
'*' * i   # 2*INT + 1*STR
#--------------------------------------------------------------------------
#review_builtin_functions  combine_map_and_Filter
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f_pow2 = lambda t: t ** 2
f_even = lambda x: x % 2 == 0

evens = filter(lambda x: x % 2 == 0, lst)
res = map(lambda t: t ** 2, evens)
map(f, lst)
# [f(1), f(2), f(3), f(4), f(5), f(6), f(7), f(8), f(9)]

print(list(res))


def my_map(fun, inp):
    out = []
    for i in inp:
        out.append(fun(i))
    return out


def my_filter(fun, inp):
    out = []
    for i in inp:
        if fun(i):
            out.append(i)
    return out
#-----------------------------------------------------------------
# filter_result
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

is_even = lambda x: x % 2 == 0

res = filter(is_even, lst)
print(list(res))
#------------------------------------------------------------------
# list_comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = lambda a: a**2
res = map(f, lst)

out_list = [a ** 2 for a in lst]
print(out_list)
out_gen = (a ** 2 for a in lst)     # makes a generator not a tuple,
# print(out)

for x in out_gen:
    print(x)
#---------------------------------------------------------------------
# map_filter
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = lambda a: (a, a ** 2, a**3)

res = map(f, lst)

# print(list(res))

for x, y, z in res:
    print(x, '+', y, '+', z, '=', x+y+z)

#-----------------------------------------------------------------------
# max_min_with_keys
lst = [(1, 9), (2, 99), (3, 0), (4, 8), (5, -106)]
# test = [9-1, 99-2, 0-3, 8-4, 6-5]
# test = [8, 97, -3, 4, 1]
f = lambda x: abs(x[1] - x[0])
res = max(lst, key=f)
print(res)

# res = max(test)
# ind = test.index(res)
# print(res, lst[ind])
#----------------------------------------------------------------------------
# review
lst = [10, 20, 30, 40, 50]
indices = [0, 1, 2, 3, 4]
# res = enumerate(lst)
# print(list(res))

for i, val in enumerate(lst):
    print(i, val)

a = [10, 20, 30, 40, 50, 60]
b = [11, 22, 33, 44, 55, 66]
c = [101, 202, 303, 404, 505, 606]

for x, y, z in zip(a, b, c):
    print(x, y, z)
#-----------------------------------------------------------------------------
# test
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# is_even = lambda x: x% 2==0
# f = lambda x: x ** 2
# out_list = [a ** 2 for a in lst if a % 2 == 0]

# out_list = [a**2 for a in range(10) if 2 < a <=


import math


def combination(n, m):
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    result = numerator / denominator
    return int(result)


out_list = [[combination(n, i) for i in range(n + 1)] for n in range(10)]

print(out_list)
#----------------------------------END---------------------------------------#



