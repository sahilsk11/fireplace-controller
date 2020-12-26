from rpi_utils import Relay, DistanceMeasurer
import json
import time

"""
Control hardware elements with added robustness than directly with GPIOl
Provides higher level of abstraction for dealing with GPIO
Designed to be called from higher order functions
"""

def turn_on():
  state = get_state()
  if state == "off":
    toggle_mode()
    update_state({"state": "on1"})
  elif state == "on1":
    toggle_mode()
    update_state({"state": "on2"})


def turn_off():
  state = get_state()
  if state == "on1":
    toggle_mode()
    time.sleep(0.5)
    toggle_mode()
  elif state == "on2":
    toggle_mode()
  update_state({"state": "off"})


def toggle_mode():
  """
  Activates fireplace switch
  """
  r = Relay()
  r.momentary()

def get_state():
  with open('states.json') as json_file:
    data = json.load(json_file)
    return data["state"]

def update_state(state_dict):
  with open('states.json', 'w') as outfile:
    json.dump(state_dict, outfile)
