# def test_var_args(farg, *args):
#     print "formal arg:", farg
#     for arg in args:
#         print "another arg:", arg
# 
# test_var_args(1, "two", 3, 6,7)


# def test_var_kwargs(farg, **kwargs):
#     print "formal arg:", farg
#     for key in kwargs:
#         print "another keyword arg: %s: %s" % (key, kwargs[key])
# 
# test_var_kwargs(farg=1, myarg2="two", myarg3=3)


# def test_var_args_call(arg1, arg2, arg3):
#     print "arg1:", arg1
#     print "arg2:", arg2
#     print "arg3:", arg3
# 
# args = ("two", 3)
# test_var_args_call(1, *args)

def tes2(arg3, arg4):
    print "arg3:", arg3
    print "arg4:", arg4
    return

def test_var_args_call(arg1, arg2=None, **kwargs):
    print "arg1:", arg1
    print "arg2", kwargs['arg2']
    tes2(**kwargs)
    

kwargs = {"arg3": 3, "arg2": "two", "arg4": "four"}
test_var_args_call(1, **kwargs)