from logging import config
import yaml


class ConfigurationLoader(object):

    @staticmethod
    def init_logger_configuration():
        with open('configs/log_config.yaml', 'r') as file:
            log_cfg = yaml.safe_load(file.read())

        config.dictConfig(log_cfg)
