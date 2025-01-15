from flask import jsonify, send_from_directory, render_template
from datetmie import datetime

app = Flask(__name__)

# Current Api Demo Version
ver = "1.0"

@app.route("/guides/intro")
def api_intro():
  return jsonify({
    "Api Ver": ver,
    "Creator": "EndlessSB is the creator of this demo",
    "Info": "This api is just a tutorial api / demo api if this endpoint is still here and has not been deleted or modified the person using it is a bit Lazy :)",
    "Time": datetime.now()
  })


    
