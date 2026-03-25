# pylint: disable=missing-module-docstring
import logging
import os
from typing import Optional

loggers = {}


def get_logger(name: str = None, log_format: Optional[str] = None):
    """
    Get custom logger instance
    """
    if name in loggers:
        return loggers[name]

    return create_logger(name=name, log_format=log_format)


def get_log_prefix():
    """
    Prepend log prefix to format if defined
    """
    log_prefix = os.getenv("LOG_PREFIX")

    if log_prefix:
        log_prefix = f"[{log_prefix}] "

    return log_prefix


def create_logger(name: str, log_format: Optional[str] = None):
    """
    Created named logger instance
    """
    if not log_format:
        log_prefix = get_log_prefix()
        log_format = f"{log_prefix}%(asctime)s - %(levelname)s - %(message)s"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    loggers[name] = logger
    return logger


root_logger = get_logger()
