from .logger_base import LoggerBase
from logging import getLogger, DEBUG
from ..handlers.configuration_loader import ConfigurationLoader


class StdoutLogger(LoggerBase):
    
    def __init__(self):
        super().__init__()
        ConfigurationLoader.init_logger_configuration()
        self._logger = getLogger('defaultLogger')
        self._logger.setLevel(DEBUG)
