from flask import Flask

flask_app_test = Flask(__name__)

@flask_app_test.route('/test')
def test():
    return "Flask app is running!"