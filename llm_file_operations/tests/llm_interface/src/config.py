import yaml
import os

class NexusConfig:
    def __init__(self, config_path='config/nexus_config.yaml'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def get_api_key(self):
        return self.config.get('anthropic_api_key')

    def get_model(self):
        return self.config.get('model', 'claude-3-5-sonnet-20240620')

    def get_max_tokens(self):
        return self.config.get('max_tokens', 1024)

# Usage example:
# config = NexusConfig()
# api_key = config.get_api_key()
# model = config.get_model()