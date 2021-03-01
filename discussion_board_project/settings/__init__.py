import os
from .base import *

env_name = os.getenv('DJANGO_SETTINGS_MODULE', 'local')

if env_name == 'prod':
    from .prod import *
else:
    from .local import *