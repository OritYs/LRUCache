import random
from infra.caches.lru_cache import LRUCache
from infra.loggers.stdout_logger import StdoutLogger
from time import sleep

MAXIMUM_COUNT = 3 * pow(10, 4)
MIN_KEY = 1
MAX_KEY = 10
MIN_VALUE = 1
MAX_VALUE = 10
MIN_CAPACITY = 1
MAX_CAPACITY = 3


def main():
    counter = 0

    stdout_logger = StdoutLogger()
    cache = LRUCache(random.randint(MIN_CAPACITY, MAX_CAPACITY), stdout_logger)
    while counter != MAXIMUM_COUNT:

        key_option = random.randint(MIN_KEY, MAX_KEY)

        if counter % 2 == 0:
            value_option = random.randint(MIN_VALUE, MAX_VALUE)
            cache.put(key_option, value_option)

        else:
            cache.get(key_option)

        counter += 1
        sleep(1)


if __name__ == "__main__":
    main()
