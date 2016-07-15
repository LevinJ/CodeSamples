


def f1(v1, v2):
    print v1, v2
    
def loadData(filename, f, args):
    print filename
    f(*args)
    print "ok"
    
loadData('we do', f1, ('v6g', 'optiserv'))