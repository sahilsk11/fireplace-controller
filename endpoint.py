import flask
import datetime
import sys
import passwords
sys.path.append("/home/pi/fireplace-controller/Sensing")
from control import toggle_mode

app = flask.Flask(__name__)

@app.route("/toggle", methods=['POST'])
def toggle_route():
  if authenticate(flask.request.json):
    toggle_mode()
    update_state(method="toggle")
    return flask.jsonify({"success": True})
  return flask.jsonify({"code": 403, "message": "Invalid credentials"})

def authenticate(data):
  if "apiKey" not in data.keys():
    return False
  return data["apiKey"] == passwords.garage_key()

def update_state(method=None, is_open=None):
  """
  Update the JSON file with new states and times after
  each API call
  """
  open_state = None
  if is_open is not None:
    #occurs when calling function uses definitive control function
    open_state = is_open
  elif method == "toggle":
    #occurs when calling function uses undefined control function
    open_state = None

  current_time = datetime.datetime.now()


if __name__ == "__main__":
  app.run()
