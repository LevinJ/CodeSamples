from random import randrange
x = (3073, 10)
for m in x:
    print m
ix = tuple([randrange(m) for m in x])
print ix