from flask import Flask, jsonify
from flask import make_response

from src.route53 import Route53

app = Flask(__name__)


@app.route('/zones/', methods=['GET'])
def list_hosted_zones():
    """ Function lists all hosted zones in Route53. """
    route53 = Route53()
    return route53.list_hosted_zones()


@app.route('/zones/<string:zone_id>', methods=['GET'])
def get_hosted_zone(zone_id):
    """
    Function return the hosted zone information

    :param zone_id: Id of hosted zone to GET record sets.
    """
    route53 = Route53()
    return route53.get_hosted_zone(zone_id=zone_id)


@app.errorhandler(404)
def not_found():
    """ If route is not defined on backend -> return 404. """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
