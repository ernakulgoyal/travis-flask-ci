"""
__license__     = "B2B-PAF"
__version__     = "0.1"
__author__      = "Nakul Goyal"
__email__       = "nakul.goyal@thepsi.com"
__copyright__   = "Copyright @2020"
__status__      = "Production/Development"
"""

from server import flask_app


def test_root_api():
    response = flask_app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World!!!'
