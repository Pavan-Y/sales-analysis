import configparser
import os

env = 'dev'

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)
env_config = config[env]