import boto3
from src.environment import Environment


class Route53():
    """ Class describes Route53 interface. """
    def __init__(self):
        """ Class constructor. """
        self.client = boto3.client(
            'route53',
            aws_access_key_id = Environment.aws_access_key,
            aws_secret_access_key = Environment.aws_secret_key
        )


    def list_hosted_zones(self):
        """ Function lists all hosted zones in Route53. """
        return self.client.list_hosted_zones()

    
    def get_hosted_zone(self, zone_id):
        """
        Function return the hosted zone information
        
        :param zone_id: Id of hosted zone to GET record sets.
        """
        return self.client.get_hosted_zone(
            Id=zone_id
        )
