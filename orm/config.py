import yaml

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        with open(self.config_file, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def __getitem__(self, key, default=None):
        return self.config.get(key, default)
    
    def __setitem__(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as file:
            yaml.dump(self.config, file)
