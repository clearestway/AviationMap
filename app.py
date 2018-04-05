from flask import Flask
from flask import render_template

@app.route('/')
def hello_world(name=None):

    return render_template('Test.html',name=name)


if __name__ == '__main__':

    app.run()

