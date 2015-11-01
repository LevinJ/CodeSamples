# -*- coding: utf-8 -*-

# a = [66.25, 333, 333, 1, 1234.5]
# print a.count(333), a.count(66.25), a.count('x')
# a.insert(2, -1)
# a.append(333)
# print a
# # print a.index(0)
# print a.pop()

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print stack
# print stack.pop()
# print stack

# from collections import deque
# 
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry") 
# queue.append("Graham")
# print queue.popleft()
# print queue.popleft()

# Functional Programming Tools¶

# def f(x):
#     return x % 3 or x % 5 ==0
# print filter(f, range(2,25))
# 
# def cube(x):
#     return x*x*x
# 
# print map(cube,range(1,11))
# 
# seq = range(8)
# def add(x,y):
#     return x+y
# print map(add, seq, seq)

# List Comprehension
squares = [x**2 for x in range(10)]
print squares
newlsit= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print newlsit

