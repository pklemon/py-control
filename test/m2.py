from __future__ import division

TIME = 0.0001

def left():
  print(TIME)

def init(mspeed):
  speed(mspeed)
  print('INIT M! called ' + str(mspeed))

def speed(val):
  global TIME
  TIME = 1/val
