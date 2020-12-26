from rpi_utils import Relay, DistanceMeasurer

"""
Control hardware elements with added robustness than directly with GPIOl
Provides higher level of abstraction for dealing with GPIO
Designed to be called from higher order functions
"""

def toggle_mode():
  """
  Activates fireplace switch
  """
  r = Relay()
  r.momentary()
