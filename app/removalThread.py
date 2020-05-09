#!/usr/bin/python

import threading
import time
import os

class removalThread(threading.Thread):
   def __init__(self, name, time):
      threading.Thread.__init__(self)
      self.toRemove = name
      self.removeDelay = time
   def run(self):
      time.sleep(self.removeDelay)
      os.remove(self.toRemove)
      return