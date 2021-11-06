from flask import Flask

from api import api

app = Flask(__name__)


def app_setup():
    app.config['DEBUG'] = True
    app.register_blueprint(api)
    return app


@app.route("/")
def hello():
    return "Hello API tester! Try the API in the route /api/data?member_id=1"


if __name__ == "__main__":
    server = app_setup()
    server.run(host='0.0.0.0', port=5001)
