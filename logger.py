import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(filename)s. %(funcName)s() line: %(lineno)d - %(message)s"


def get_file_handler(log_name):
    file_handler = logging.FileHandler(log_name)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name, log_name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(log_name))
    logger.addHandler(get_stream_handler())
    return logger
