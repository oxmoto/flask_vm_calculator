from flask import Flask

app = Flask(__name__)

from . import routes

# Load configuration from JSON file or set default parameters
def load_config():
    import json
    import os

    config_file = 'config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "nbr_hosts": 2,
            "reservation": 20,
            "host_nbr_core": 10,
            "host_nbr_ram": 256,
            "vm_nbr_core": 2,
            "vm_nbr_ram": 4,
        }

app.config['PARAMETERS'] = load_config()
