import pickle
import resource
import sys

print resource.getrlimit(resource.RLIMIT_STACK)
print sys.getrecursionlimit()

max_rec = 0x100000

# May segfault without this line. 0x100 is a guess at the size of each stack frame.
resource.setrlimit(resource.RLIMIT_STACK, [0x100 * max_rec, resource.RLIM_INFINITY])
sys.setrecursionlimit(max_rec)

a = []
# 0x10 is to account for subfunctions called inside `pickle`.
for i in xrange(max_rec / 0x10):
    a = [a]
print pickle.dumps(a, -1)