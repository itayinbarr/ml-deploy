import logging
import logging.config

def setup_logging():
    logging.config.fileConfig('src/logging.conf')
    logger = logging.getLogger('mlModelLogger')
    return logger
