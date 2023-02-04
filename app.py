from flask import Flask, render_template
import jsonify
import os
from winner import main



app = Flask(__name__, template_folder="templates", static_folder="/")
os.environ['FLASK_APP'] = "app.py"

@app.route("/", methods=['GET'])
def scoreboard():
    main()
    return render_template("index.html")