#if statement
# x = int(raw_input("Please enter an integer: "))
# if x<0:
#     x=0
#     print 'negative value changed to zero'
# elif x==0:
#     print 'zero'
# else:
#     print 'More'
#     
# #for statement
# words = ['cat', 'window', 'defenestrate']
# for w in words[:]:    # Loop over a slice copy of the entire list.
#     if len(w) > 6:
#         print w, len(w)
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print i, a[i]


# for num in range(2, 10):
#     if num % 2 == 0:
#         print "Found an even number", num
#         continue
#     print "Found an odd number",num

# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print a
#         a, b = b, a+b
# fib(2000)

# def fib2(n):
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)    # see below
#         a, b = b, a+b
#     return result
# print fib2(100) 

# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     """this is a documentation strin"""
#     while True:
#         ok = raw_input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise IOError('refusenik user')
#         print complaint
# print ask_ok.__doc__
# List - a mutable type
# def try_to_change_list_contents(the_list):
#     print 'got', the_list
#     the_list.append('four')
#     print 'changed to', the_list
# 
# outer_list = ['one', 'two', 'three']
# 
# print 'before, outer_list =', outer_list
# try_to_change_list_contents(outer_list)
# print 'after, outer_list =', outer_list
# 
# 
# def try_to_change_list_reference(the_list):
#     print 'got', the_list
#     the_list = ['and', 'we', 'can', 'not', 'lie']
#     print 'set to', the_list
# 
# outer_list = ['we', 'like', 'proper', 'English']
# 
# print 'before, outer_list =', outer_list
# try_to_change_list_reference(outer_list)
# print 'after, outer_list =', outer_list

def try_to_change_int(the_int):
#     print 'got', the_int
#     the_int=6
#     print 'changed to', the_int
    return ["this is funny",5,6]

the_int= 5
# try_to_change_int(the_int)
# print 'after, outer_int =', the_int
print try_to_change_int(the_int)[0]
print try_to_change_int(the_int)[1]
