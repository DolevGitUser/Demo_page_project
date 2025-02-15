import logging

class CustomFormatter(logging.Formatter):
    """Custom formatter adding color to log levels"""
    grey = "\x1b[38;21m"
    blue = "\x1b[34;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + "%(asctime)s - %(levelname)s - %(message)s" + reset,
        logging.INFO: blue + "%(asctime)s - %(levelname)s - %(message)s" + reset,
        logging.WARNING: yellow + "%(asctime)s - %(levelname)s - %(message)s" + reset,
        logging.ERROR: red + "%(asctime)s -  %(levelname)s - %(message)s" + reset,
        logging.CRITICAL: bold_red + "%(asctime)s -  %(levelname)s - %(message)s" + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

def get_logger():
    """Returns the logger instance with enhanced formatting"""
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    return logger