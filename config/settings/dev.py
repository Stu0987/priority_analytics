import os
from .base import *

DEBUG = os.getenv("DEBUG", "False").lower() == "true"