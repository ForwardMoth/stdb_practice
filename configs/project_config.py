import yaml


class Config:
    """Класс считывает базовые настройки из файла config.yaml"""

    def __init__(self):
        with open('configs/config.yaml') as f:
            config = yaml.safe_load(f)['database']
            self.user = config['user']
            self.password = config['password']
            self.db_name = config['db_name']
            self.port = config["port"]

