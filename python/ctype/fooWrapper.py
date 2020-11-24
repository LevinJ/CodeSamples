import  ctypes

lib = ctypes.cdll.LoadLibrary('./build/libfoo.so')


obj = lib.Foo_new()
lib.Foo_bar(obj)
# lib.Foo_bar_3(obj, 3)
# lib.Foo_bar_2(obj, b'this is incredible')

print("we are good")
# name = b"Frank"
# c_name = ctypes.c_char_p(name)
# foo = lib.hello(c_name)
# # print (c_name.value )# this comes back fine
# print ("return value = {}".format(ctypes.c_char_p(foo).value ))# segfault
# 
# lib.free_mem()
# print('memory freeed!')