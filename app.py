from flask import Flask
from flask import render_template,send_from_directory
import Data_Server
# initializes a flask app
app = Flask(__name__)
# has the Data_Server function refresh the files served to the server
a=Data_Server.aviation_data()
print a
# responded for each path accessed by a web page
@app.route('/')
def aviation(name=None):
    return render_template('Test.html',name=name),

@app.route("/sigmet.JSON")
def sigmet(name=None):
    return render_template('sigmet_data.JSON')
@app.route("/aircraft.JSON")
def aircraft(name=None):
    return render_template('aircraftrep_data.JSON')

@app.route("/metar.JSON")
def metar(name=None):
    return render_template('metar_data.JSON')

@app.route("/airmet.JSON")
def airmet(name=None):
    return render_template('airmet_data.JSON')
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(path)


if __name__ == '__main__':
    app.run()

