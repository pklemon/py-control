#!/usr/bin/env python
# coding: utf8

import pigpio

pi = pigpio.pi('10.10.1.4')

L1 = 26
L2 = 19
L3 = 13
L4 = 6
L5 = 5
L6 = 11

def l1_on():
  pi.write(L1, 0)

def l2_on():
  pi.write(L2, 0)

def l3_on():
  pi.write(L3, 0)

def l4_on():
  pi.write(L4, 0)

def l5_on():
  pi.write(L5, 0)

def l6_on():
  pi.write(L6, 0)

def l1_off():
  pi.write(L1, 1)

def l2_off():
  pi.write(L2, 1)

def l3_off():
  pi.write(L3, 1)

def l4_off():
  pi.write(L4, 1)

def l5_off():
  pi.write(L5, 1)

def l6_off():
  pi.write(L6, 1)