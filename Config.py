class Config(object):

    _instance = None

    def __init__(self):
        self._data = Config.parse_conf_file('scanner.conf')

    @staticmethod
    def instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    @staticmethod
    def parse_conf_file(file_path):
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()
                # Skip empty lines or comments
                if not line or line.startswith('#'):
                    continue
                # Split the line by '=' and strip whitespace
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
        return config

    def get(self, key):
        return self._data[key]