from flask import Flask, jsonify
from flask import make_response


app = Flask(__name__)


@app.errorhandler(404)
def not_found():
    """ If route is not defined on backend -> return 404. """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
