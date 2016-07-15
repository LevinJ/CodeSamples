from collections import defaultdict

qTable = defaultdict(int)
inputs = {'light': 'green', 'oncoming': None, 'right': None, 'left': None}
next_waypoint = "right"
action = 'left'
qTable[(inputs['light'],next_waypoint,action)] = 1
print qTable

qTable[(inputs['light'],action,next_waypoint,None)] = 2
print qTable

qTable[(inputs['light'],action,None,next_waypoint)] = 2
print qTable