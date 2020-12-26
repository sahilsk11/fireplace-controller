import flask
import datetime
import sys
import passwords
sys.path.append("/home/pi/fireplace-controller/Sensing")
from control import toggle_mode, turn_on, turn_off

app = flask.Flask(__name__)

@app.route("/toggle", methods=['GET', 'POST'])
def toggle_route():
  if authenticate(flask.request.json):
    toggle_mode()
    update_state(method="toggle")
    return flask.jsonify({"success": True})
  return flask.jsonify({"code": 403, "message": "Invalid credentials"})


@app.route("/on", methods=['GET', 'POST'])
def toggle_route():
  if authenticate(flask.request.json):
    turn_on()
    return flask.jsonify({"success": True})
  return flask.jsonify({"code": 403, "message": "Invalid credentials"})


@app.route("/off", methods=['GET', 'POST'])
def toggle_route():
  if authenticate(flask.request.json):
    turn_off()
    return flask.jsonify({"success": True})
  return flask.jsonify({"code": 403, "message": "Invalid credentials"})

def authenticate(data):
  return True
  if "apiKey" not in data.keys():
    return False
  return data["apiKey"] == passwords.garage_key()


if __name__ == "__main__":
  app.run(debug=True)
