import os
import json

CONFIG_DIR = os.path.expanduser('~/shai')
CONFIG_FILE = os.path.join(CONFIG_DIR, '.shai-config.json')

class Config:
    def __init__(self):
        self.config = {}
        self.load_config()
    
    def create_config(self):
        if not os.path.exists(CONFIG_DIR):
            os.mkdir(CONFIG_DIR)
        API_KEY = input('Enter your API key: ')
        config_data = {'api_key': API_KEY}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f)

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            self.create_config()
        with open(CONFIG_FILE, 'r') as f:
            self.config = json.load(f)

    def get_api_key(self):
        return self.config['api_key']