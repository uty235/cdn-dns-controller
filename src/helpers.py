import random
import string


class Helper:
    """ Helper function just to do some stuff. """
    def get_random_string(self, length):
        """ Function to generate random string. """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
