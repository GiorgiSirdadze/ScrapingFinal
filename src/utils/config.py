import yaml

def load_config(path="config/settings.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)
