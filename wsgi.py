import sys

sys.path.append("/var/www/app/")
from app import create_app

application = create_app()
