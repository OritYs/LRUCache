from configparser import ConfigParser


class CacheConfigReader:

    def __init__(self):
        self.__config_object = ConfigParser()
        self.__config_object.read("configs/cache_config.ini")

    def get_int(self, section_name, key):
        return int(self.__config_object.get(section_name, key))
