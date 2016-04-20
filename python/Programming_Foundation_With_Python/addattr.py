import numpy as np

class empty:
    def __init__(self):
        self.var1 = 'hello'
        return


e = empty()

e.foo = 'foovar'


a = np.arange(10)
a.newvar = 'hellow rold'
print(a)
print(e.foo)
print(e.var1)