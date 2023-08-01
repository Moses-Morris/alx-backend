#!/usr/bin/env python3
'''Flask Application'''

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Flask app configurations'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    '''render the template'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run
