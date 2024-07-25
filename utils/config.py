import yaml

def load_config():
    with open("configs/config.yaml", 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)
    return config
