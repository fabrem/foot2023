from flask import Flask, render_template
# import jsonify
import os
from src.winner import main



app = Flask(__name__, template_folder="templates", static_folder="/")
os.environ['FLASK_APP'] = "app.py"

@app.route("/", methods=['GET'])
def scoreboard():
    main()
    return render_template("index.html")

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=5000, debug=True)
