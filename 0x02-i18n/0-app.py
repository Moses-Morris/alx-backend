#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' return the template '''
    title = "Welcome to Holberton"
    greeting = "Hello world"
    return render_template('0-index.html', title=title, greeting=greeting)


if __name__ == '__main__':
    app.run()
