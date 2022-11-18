import yaml

class ProjectConfig:
    """Класс считывает базовые настройки из файла config.yaml"""

    def __init__(self):
        with open('config.yaml') as f:
            config = yaml.safe_load(f)
            self.dbfilepath = config['dbfilepath']
            self.dbtableprefix = config['dbtableprefix']
            self.user = config['user']
            self.password = config['password']
            self.db_name = config['db_name']

if __name__ == "__main__":
    x = ProjectConfig()
    print(x.dbfilepath)
