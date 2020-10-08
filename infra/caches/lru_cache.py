from collections import OrderedDict
from ..handlers.validation import Validation
from ..handlers.cache_config_reader import CacheConfigReader
import logging


class LRUCache:

    def __init__(self, capacity, logger):
        self.__config_reader = CacheConfigReader()
        if Validation.positive_validation(capacity) and \
                Validation.range_validation(capacity, self.__config_reader.get_int("CAPACITY", "min"),
                                            self.__config_reader.get_int("CAPACITY", "max")):
            self.__capacity = capacity
        else:
            self.__capacity = self.__config_reader.get_int("CAPACITY", "min")

        self.__ordered_dictionary = OrderedDict()
        self.__logger = logger
        self.__counter = 0

    def get(self, key):
        if key in self.__ordered_dictionary:
            self.__ordered_dictionary.move_to_end(key)
            self.__logger.send_log_message(log_level=logging.INFO,
                                           message="The key " + str(key) + " has been searched")
            return self.__ordered_dictionary.get(key)

        return self.__config_reader.get_int("DEFAULT_VALUES", "not_found_value")

    def put(self, key, value):
        if key in self.__ordered_dictionary:
            self.__ordered_dictionary.move_to_end(key)
        else:
            if self.__counter == self.__capacity:
                self.__ordered_dictionary.popitem(last=False)
                self.__counter -= 1

            self.__counter += 1
        if Validation.range_validation(key, self.__config_reader.get_int("KEY", "min"),
                                       self.__config_reader.get_int("KEY", "max")):
            if Validation.range_validation(value, self.__config_reader.get_int("KEY", "min"),
                                            self.__config_reader.get_int("KEY", "max")):
                self.__ordered_dictionary[key] = value
                self.__logger.send_log_message(log_level=logging.DEBUG,
                                               message="The key " + str(key) + " has been updated")
