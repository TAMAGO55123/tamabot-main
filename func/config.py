import yaml

setting_file_path = "../setting/main.yaml"

def load_config(key:str) -> object:
    print(__file__)
    with open(setting_file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config[key]