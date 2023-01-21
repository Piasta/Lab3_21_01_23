import logging


def get_logs(level, format_string, log_level):
    logging.basicConfig(level=level, format=format_string)
    logger = logging.getLogger()
    logger.setLevel(log_level)
    return logger


print("----Input your logging level. (debug/info/warning/error/critical)----")
user_level = input().upper()
logger = get_logs(logging.DEBUG, '%(asctime)s - %(name)s - %(levelname)s - %(message)s', log_level=user_level)

if user_level == 'DEBUG':
    logger.debug("This is a debug message.")
if user_level == 'INFO':
    logger.info("This is an informational message.")
if user_level == 'WARNING':
    logger.warning("This is a warning message.")
if user_level == 'ERROR':
    logger.error("This is an error message.")
if user_level == 'CRITICAL':
    logger.critical("This is a critical message.")
