from ctypes import cdll
import  ctypes
lib = cdll.LoadLibrary('./build/libfoo.so')


obj = lib.Foo_new()
lib.Foo_bar(obj)
lib.Foo_bar_3(obj, 3)
lib.Foo_bar_2(obj, b'this is incredible')