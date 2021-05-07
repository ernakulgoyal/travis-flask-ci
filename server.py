"""
__license__     = "B2B-PAF"
__version__     = "0.1"
__author__      = "Nakul Goyal"
__email__       = "nakul.goyal@thepsi.com"
__copyright__   = "Copyright @2020"
__status__      = "Production/Development"
"""

from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")
def say_hello():
    return "Hello World!!!"


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0')
