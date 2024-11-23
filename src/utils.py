import configparser
# from dotenv import load_dotenv
from dotenv import dotenv_values
# import os
from pathlib import Path


def load_config () -> dict:
    setting_file_path = get_file_config()['setting_file_path']

    config = configparser.ConfigParser()
    config.read(setting_file_path)
    config_dict = {}
    env_var = load_env()

    for k,v in config.items():
        config_dict[k] = v

    # Assign sensitive information from .env to config setting

    config_dict['KAFKA_PROD_SERVER']['bootstrap.servers'] = env_var['KAFKA_PROD_SERVER']
    config_dict['KAFKA_PROD_SERVER']['sasl.username'] = env_var['KAFKA_PROD_SASL_USERNAME']
    config_dict['KAFKA_PROD_SERVER']['sasl.password'] = env_var['KAFKA_PROD_SASL_PASSWORD']
    
    config_dict['KAFKA_DEV_SERVER']['bootstrap.servers'] = env_var['KAFKA_LOCAL_SERVER']
    config_dict['KAFKA_DEV_SERVER']['sasl.username'] = env_var['KAFKA_LOCAL_SASL_USERNAME']
    config_dict['KAFKA_DEV_SERVER']['sasl.password'] = env_var['KAFKA_LOCAL_SASL_PASSWORD']

    return config_dict



def load_env() -> dict: 
    env_file_path = get_file_config()['env_file_path']
    return dotenv_values(env_file_path)
        
def get_file_config() -> dict:
    # Get current file location and return back 2 levels 
    BASE_DIR = Path(__file__).parent.parent

    # Get abs path of .env
    env_file_path = BASE_DIR.joinpath('config/.env').absolute()
    # Get abs path of setting.ini
    setting_file_path = BASE_DIR.joinpath('config/setting.ini').absolute()
    return {'env_file_path' : env_file_path , 'setting_file_path' : setting_file_path }


# print(get_file_config())

# print(dict(load_config()['KAFKA_PROD_SERVER']))
# print(dict(load_config()['KAFKA_DEV_SERVER']))

# print(load_env())
# print(load_config(config_env='KAFKA_DEV_SERVER'))