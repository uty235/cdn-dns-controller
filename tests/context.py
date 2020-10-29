""" Pytest configuration. """
from __future__ import absolute_import

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.environment import Environment
from main import app 
from src.route53 import Route53
