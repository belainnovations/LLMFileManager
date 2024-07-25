import yaml
import os

class NexusConfig:
    def __init__(self, config_path='config/nexus_config.yaml'):
        self.config_path = config_path
        self._config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        required_fields = ['api_key', 'model', 'max_tokens']
        for field in required_fields:
            if field not in config:
                raise ValueError(f"Missing required field '{field}' in config file")

        return config

    def get_api_key(self):
        return self._config['api_key']

    def get_model(self):
        return self._config['model']

    def get_max_tokens(self):
        return self._config['max_tokens']

# Usage example:
# config = NexusConfig()
# api_key = config.get_api_key()
# model = config.get_model()
