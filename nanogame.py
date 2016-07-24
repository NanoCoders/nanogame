from processing import *
from time import sleep
from math import *
from random import randint

def setup():
  frameRate(30)
  size(400, 400)

class Storage:
  def __init__ (self):
    pass

# You can store whatever you want in this object
Variables = Storage()

# Sprite object class
class Sprite:
  def __init__ (self, x, y, height, width):
    self.x = x
    self.y = y
    self.v = 0
    self.height = height
    self.width = width

  def color(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def display(self):
    stroke(0)
    fill(self.r, self.g, self.b)
    rectMode(CENTER)
    rect(self.x, self.y, self.width, self.height)

  # Easy collision detection
  def isTouching(self, sprite2):
    if (self.x < self.x < sprite2.x + 75):

      if (self.y < sprite2.y - 75) or (self.y > sprite2.y + 75):
        print "Bird died!"
    else:
      pass


# Reusable wall class that can be used in other games
class Wall:
  def __init__ (self, speed, spacing, r, g, b):
    self.speed = speed
    self.spacing = spacing
    self.r = r
    self.g = g
    self.b = b
    self.x = 400
    self.y = randint(10 + self.spacing, 400 - (10 + self.spacing))

  def color(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def display(self):
    rectMode(CORNER)

    stroke(80)
    fill(self.r, self.g, self.b)

    rect(self.x, self.y - (400 + self.spacing), 75, 400)
    rect(self.x, self.y + self.spacing, 75, 400)



run()
