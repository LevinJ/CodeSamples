import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random


client = carla.Client('localhost', 2000)

client.set_timeout(10.0) # seconds

world = client.get_world()

print(client.get_available_maps())
world = client.load_world('Town01')