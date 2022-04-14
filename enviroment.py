import os


class Environment:
    LOGS = False
    DEV = "dev"
    PROD = 'prod'

    URLS = {
        DEV: 'https://playground.learnqa.ru/ajax/api/api_dev',
        PROD: 'https://playground.learnqa.ru/ajax/api/api'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of environment {self.env}")


ENV_OBJECT = Environment()
