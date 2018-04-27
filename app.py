from flask import Flask
from flask import render_template
from flask import send_file
import Data_Server

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()

